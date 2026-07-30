# Publicación de experiencias de laboratorio en Canvas

Estos scripts publican exclusivamente los documentos de `lab/`. No suben
cátedras semanales.

## Estructura local

Cada experiencia debe tener un directorio único:

```text
lab/
└── experiencia01-nombre-breve/
    ├── guia-estudiante.pdf
    ├── rubrica.pdf
    └── template-reporte.docx
```

Los nombres pueden variar, pero deben contener:

- `guia` para la guía de la experiencia y sus materiales;
- `rubrica` para la rúbrica;
- `template` o `plantilla` para el documento del reporte.

Se admite PDF, DOCX, XLSX, XLS, CSV y PPTX. Debe existir exactamente un
documento de cada categoría. La guía docente no se publica.

Los directorios auxiliares `build/`, `tmp/` y `__pycache__/` se ignoran al
buscar documentos. Así, una copia compilada dentro de `build/` no se confunde
con el PDF final.

Las presentaciones Beamer se conservan en `lab/slides_expXX/`, fuera de
`experienciaXX-*`. El script no busca ni sube esas carpetas. Por tanto, esta
separación no requiere cambiar el código de publicación.

Una carpeta que contenga el marcador `NO_PUBLICAR` puede probarse normalmente
sin `--produccion`, pero el script rechazará cualquier intento de publicarla.

## Resultado en Canvas

Para `experiencia01-ley-de-ohm`, el script crea:

```text
Experiencia 01 | ley de ohm
├── Guía Experiencia 01
├── Rúbrica Reporte 01
├── Template Reporte 01
└── Entrega Experiencia 01
```

El modo de prueba utiliza este mismo módulo, pero lo deja sin publicar. Si el
módulo ya está publicado, el modo de prueba se detiene para no modificar
contenido visible. `--produccion` publica el módulo y sus items.

La tarea de entrega se crea automáticamente; no se necesita
`--crear-entrega`. Sus valores predeterminados son:

- título `Entrega Experiencia XX`;
- vencimiento 14 días después de ejecutar la subida, a las 23:30 de Santiago;
- 7 puntos;
- carga en línea de archivos PDF;
- 2 intentos;
- entrega individual.

Los valores pueden ajustarse con `--titulo-entrega`, `--dias-entrega`,
`--hora-cierre`, `--puntos`, `--extensiones` e `--intentos`. La modalidad
grupal no se activa hasta que el curso tenga definido un conjunto de grupos
en Canvas.

## Uso

```bash
python -m pip install -r scripts_canvas/requirements.txt
```

El argumento principal es `--experiencia`; `--exp` es su alias corto:

```bash
python scripts_canvas/subir_experiencia.py \
  --experiencia 1 \
  --usuarios Profesor
```

Equivalente:

```bash
python scripts_canvas/subir_experiencia.py --exp 1 --usuarios Profesor
```

Producción:

```bash
python scripts_canvas/subir_experiencia.py \
  --exp 1 \
  --usuarios Profesor \
  --produccion
```

Títulos visibles opcionales:

```bash
python scripts_canvas/subir_experiencia.py \
  --exp 1 \
  --usuarios Profesor \
  --titulo-modulo "Experiencia 01 | Ley de Ohm" \
  --titulo-guia "Guía: medición de voltaje en una resistencia" \
  --titulo-rubrica "Rúbrica del reporte 01" \
  --titulo-template "Plantilla del reporte 01"
```

Variables opcionales:

- `CANVAS_KEY_FILE`: ruta a las credenciales.
- `CANVAS_LAB_DIR`: directorio que contiene las experiencias.

`Key.txt` mantiene el formato:

```text
Profesor|TokenCanvas|CourseID
```

Además de los tres documentos, cada ejecución crea o actualiza la tarea de
entrega del mismo módulo. Si se vuelve a ejecutar, el script reutiliza la
tarea con el mismo nombre en vez de duplicarla.
