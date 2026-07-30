"""Publicación segura de experiencias de laboratorio en Canvas."""

import os
import re
import unicodedata
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from canvasapi import Canvas


CANVAS_URL = "https://canvas.unab.cl/"
REPO_ROOT = Path(__file__).resolve().parents[1]
LAB_BASE_PATH = Path(os.getenv("CANVAS_LAB_DIR", REPO_ROOT / "lab"))
SUPPORTED_SUFFIXES = {".pdf", ".docx", ".xlsx", ".xls", ".csv", ".pptx"}
IGNORED_CONTENT_DIRS = {"build", "tmp", "__pycache__"}
CANVAS_TIMEZONE = ZoneInfo("America/Santiago")

canvas = None
current_user_name = None
current_course_id = None


def _cargar_usuarios_desde_texto(config_path=None):
    """Carga líneas ``profesor|token|course_id`` desde Key.txt."""
    default_path = Path(__file__).with_name("Key.txt")
    path = Path(config_path or os.getenv("CANVAS_KEY_FILE", default_path))
    if not path.is_file():
        print(f"⚠ Archivo de configuración no encontrado: {path}")
        return {}

    users = {}
    with path.open("r", encoding="utf-8") as fh:
        for line_number, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = [part.strip() for part in line.split("|")]
            if len(parts) < 2 or not parts[0] or not parts[1]:
                print(f"⚠ Línea {line_number} inválida en {path}")
                continue
            nombre, token = parts[0], parts[1]
            users[nombre] = token
            if len(parts) >= 3 and parts[2]:
                try:
                    users[f"{nombre}_id"] = int(parts[2])
                except ValueError:
                    print(f"⚠ course_id inválido en línea {line_number}")
    return users


USERS = _cargar_usuarios_desde_texto()


def select_user(nombre_usuario):
    """Conecta con Canvas usando un usuario configurado en Key.txt."""
    global canvas, current_user_name, current_course_id
    if nombre_usuario not in USERS:
        print(f"❌ Usuario no configurado: {nombre_usuario}")
        return False

    token = USERS[nombre_usuario]
    current_course_id = USERS.get(f"{nombre_usuario}_id")
    if current_course_id is None:
        print(f"❌ El usuario {nombre_usuario} no tiene course_id configurado")
        return False

    try:
        canvas = Canvas(CANVAS_URL, token)
        user = canvas.get_current_user()
        current_user_name = user.name
        print(f"✓ Conectado como: {current_user_name}")
        print(f"✓ Course ID: {current_course_id}")
        return True
    except Exception as exc:
        print(f"❌ Error al conectar con Canvas: {exc}")
        canvas = None
        current_user_name = None
        current_course_id = None
        return False


def _normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(char for char in texto if not unicodedata.combining(char))
    return texto.lower()


def _resolver_directorio_experiencia(numero_experiencia):
    """Encuentra un único directorio ``experienciaXX-nombre`` dentro de lab/."""
    if numero_experiencia < 1:
        print("❌ El número de experiencia debe ser mayor que cero")
        return None
    if not LAB_BASE_PATH.is_dir():
        print(f"❌ Directorio de laboratorio no encontrado: {LAB_BASE_PATH}")
        return None

    patron = re.compile(r"^experiencia\s*0*(\d+)(?:[-_\s].*)?$", re.IGNORECASE)
    encontrados = []
    for path in LAB_BASE_PATH.iterdir():
        if not path.is_dir():
            continue
        match = patron.match(path.name)
        if match and int(match.group(1)) == numero_experiencia:
            encontrados.append(path)

    if not encontrados:
        print(
            f"❌ No se encontró la experiencia {numero_experiencia}. "
            f"Se esperaba {LAB_BASE_PATH}/experiencia{numero_experiencia:02d}-nombre/"
        )
        return None
    if len(encontrados) > 1:
        print("❌ Hay más de un directorio para la misma experiencia:")
        for path in encontrados:
            print(f"   - {path}")
        return None
    return encontrados[0]


def _titulo_modulo_desde_directorio(path, numero_experiencia):
    nombre = re.sub(
        r"^experiencia\s*0*\d+(?:[-_\s]+)?",
        "",
        path.name,
        flags=re.IGNORECASE,
    )
    nombre = re.sub(r"[-_]+", " ", nombre).strip()
    base = f"Experiencia {numero_experiencia:02d}"
    return f"{base} | {nombre}" if nombre else base


def _clasificar_documentos(path):
    """Obtiene guía, rúbrica y template; exige exactamente uno de cada tipo."""
    candidatos = [
        file
        for file in path.rglob("*")
        if (
            file.is_file()
            and file.suffix.lower() in SUPPORTED_SUFFIXES
            and not any(
                part.lower() in IGNORED_CONTENT_DIRS
                for part in file.relative_to(path).parts[:-1]
            )
        )
    ]
    categorias = {"guia": [], "rubrica": [], "template": []}
    for file in candidatos:
        nombre = _normalizar(file.stem)
        if "guia" in nombre and "docente" not in nombre:
            categorias["guia"].append(file)
        if "rubrica" in nombre:
            categorias["rubrica"].append(file)
        if "template" in nombre or "plantilla" in nombre:
            categorias["template"].append(file)

    errores = False
    for categoria, files in categorias.items():
        if len(files) == 1:
            continue
        errores = True
        if not files:
            print(f"❌ Falta un documento de tipo '{categoria}' en {path}")
        else:
            print(f"❌ Hay varios documentos candidatos para '{categoria}':")
            for file in files:
                print(f"   - {file}")
    return None if errores else {key: files[0] for key, files in categorias.items()}


def _buscar_modulo(course, module_name):
    for module in course.get_modules():
        if module.name == module_name:
            return module
    return None


def _buscar_entrega(course, assignment_name):
    """Encuentra una única tarea con el nombre exacto indicado."""
    encontradas = [
        assignment
        for assignment in course.get_assignments(search_term=assignment_name)
        if assignment.name == assignment_name
    ]
    if len(encontradas) > 1:
        print(f"❌ Hay varias tareas llamadas '{assignment_name}' en Canvas")
        return False
    return encontradas[0] if encontradas else None


def _calcular_vencimiento(dias, hora_cierre, ahora=None):
    """Calcula el cierre en hora de Santiago a partir del día de la subida."""
    ahora = ahora or datetime.now(CANVAS_TIMEZONE)
    fecha = (ahora.astimezone(CANVAS_TIMEZONE) + timedelta(days=dias)).date()
    return datetime.combine(
        fecha,
        time(hour=hora_cierre[0], minute=hora_cierre[1]),
        tzinfo=CANVAS_TIMEZONE,
    )


def subir_experiencia(
    numero_experiencia,
    course_id=None,
    test_mode=True,
    titulo_modulo=None,
    titulos_documentos=None,
    titulo_entrega=None,
    dias_entrega=14,
    hora_cierre=(23, 30),
    puntos_entrega=7,
    extensiones_entrega=None,
    intentos_entrega=2,
):
    """Publica documentos y una tarea de entrega dentro del módulo."""
    if canvas is None:
        print("❌ No hay conexión activa con Canvas")
        return None
    course_id = course_id or current_course_id
    if course_id is None:
        print("❌ No hay course_id disponible")
        return None

    experiencia_dir = _resolver_directorio_experiencia(numero_experiencia)
    if experiencia_dir is None:
        return None
    if not test_mode and (experiencia_dir / "NO_PUBLICAR").exists():
        print(
            f"❌ {experiencia_dir.name} está marcada con NO_PUBLICAR. "
            "Solo puede utilizarse en modo de prueba."
        )
        return None
    documentos = _clasificar_documentos(experiencia_dir)
    if documentos is None:
        print("💡 No se modificará Canvas hasta completar la estructura local.")
        return None

    module_name = (
        titulo_modulo.strip()
        if titulo_modulo
        else _titulo_modulo_desde_directorio(experiencia_dir, numero_experiencia)
    )
    if not module_name:
        print("❌ El título del módulo no puede estar vacío")
        return None

    assignment_name = (
        titulo_entrega.strip()
        if titulo_entrega
        else f"Entrega Experiencia {numero_experiencia:02d}"
    )
    if not assignment_name:
        print("❌ El título de la entrega no puede estar vacío")
        return None
    extensiones_entrega = list(extensiones_entrega or ["pdf"])
    due_at = _calcular_vencimiento(dias_entrega, hora_cierre)

    titulos = {
        "guia": f"Guía Experiencia {numero_experiencia:02d}",
        "rubrica": f"Rúbrica Reporte {numero_experiencia:02d}",
        "template": f"Template Reporte {numero_experiencia:02d}",
    }
    for categoria, titulo in (titulos_documentos or {}).items():
        if categoria not in titulos:
            print(f"❌ Categoría de título no válida: {categoria}")
            return None
        titulo = titulo.strip()
        if not titulo:
            print(f"❌ El título de {categoria} no puede estar vacío")
            return None
        titulos[categoria] = titulo

    course = canvas.get_course(course_id)
    module = _buscar_modulo(course, module_name)
    if test_mode and module is not None and getattr(module, "published", False):
        print(
            f"❌ El módulo '{module_name}' ya está publicado. "
            "El modo de prueba no modificará un módulo visible."
        )
        return None
    assignment = _buscar_entrega(course, assignment_name)
    if assignment is False:
        return None
    if (
        test_mode
        and assignment is not None
        and getattr(assignment, "published", False)
    ):
        print(
            f"❌ La tarea '{assignment_name}' ya está publicada. "
            "El modo de prueba no modificará una tarea visible."
        )
        return None

    print("=" * 80)
    print("🧪 SUBIENDO EXPERIENCIA DE LABORATORIO")
    print(f"Experiencia: {numero_experiencia:02d}")
    print(f"Directorio: {experiencia_dir}")
    print(f"Módulo: {module_name}")
    print(f"Modo: {'PRUEBA (no publica)' if test_mode else 'PRODUCCIÓN (publica)'}")
    for categoria in ("guia", "rubrica", "template"):
        print(f"  {categoria}: {documentos[categoria].name} → {titulos[categoria]}")
    print(f"  entrega: {assignment_name}")
    print(f"    vencimiento: {due_at.isoformat()}")
    print(f"    puntaje: {puntos_entrega:g}")
    print(f"    formato: {', '.join(extensiones_entrega)}")
    print(f"    intentos: {intentos_entrega}")
    print("    modalidad: individual")
    print("=" * 80)

    # Todos los archivos se cargan antes de reemplazar items del módulo.
    uploads = {}
    try:
        for categoria in ("guia", "rubrica", "template"):
            response = course.upload(str(documentos[categoria]))
            uploads[categoria] = response[1]["id"]
            print(f"✓ Archivo cargado: {documentos[categoria].name}")
    except Exception as exc:
        print(f"❌ Falló la carga previa; el módulo no fue reemplazado: {exc}")
        return None

    if module is None:
        module = course.create_module(
            module={
                "name": module_name,
                "published": not test_mode,
            }
        )
        print(f"✓ Módulo creado: {module_name}")

    assignment_data = {
        "name": assignment_name,
        "submission_types": ["online_upload"],
        "allowed_extensions": extensiones_entrega,
        "points_possible": puntos_entrega,
        "grading_type": "points",
        "due_at": due_at.isoformat(),
        "allowed_attempts": intentos_entrega,
        "published": not test_mode,
    }
    try:
        if assignment is None:
            assignment = course.create_assignment(assignment=assignment_data)
            print(f"✓ Tarea creada: {assignment_name}")
        else:
            assignment.edit(assignment=assignment_data)
            print(f"✓ Tarea actualizada: {assignment_name}")
    except Exception as exc:
        print(f"❌ No se pudo crear o actualizar la tarea: {exc}")
        return None

    titulos_objetivo = set(titulos.values())
    for item in list(module.get_module_items()):
        if item.type == "File" and item.title in titulos_objetivo:
            item.delete()
            print(f"✓ Versión anterior retirada del módulo: {item.title}")
        if (
            item.type == "Assignment"
            and (
                item.title == assignment_name
                or getattr(item, "content_id", None) == assignment.id
            )
        ):
            item.delete()
            print(f"✓ Versión anterior retirada del módulo: {item.title}")

    for position, categoria in enumerate(("guia", "rubrica", "template"), start=1):
        item = module.create_module_item(
            module_item={
                "type": "File",
                "content_id": uploads[categoria],
                "title": titulos[categoria],
                "position": position,
                "indent": 0,
                "published": not test_mode,
            }
        )
        try:
            item.edit(module_item={"published": not test_mode})
        except Exception:
            pass
        print(f"✓ Item agregado: {titulos[categoria]}")

    assignment_item = module.create_module_item(
        module_item={
            "type": "Assignment",
            "content_id": assignment.id,
            "title": assignment_name,
            "position": 4,
            "indent": 0,
            "published": not test_mode,
        }
    )
    try:
        assignment_item.edit(module_item={"published": not test_mode})
    except Exception:
        pass
    print(f"✓ Item agregado: {assignment_name}")

    if not test_mode:
        module.edit(module={"published": True})
        print("✓ Módulo publicado")
    else:
        print("✓ Módulo conservado sin publicar")

    return module
