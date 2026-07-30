#!/usr/bin/env python3
"""Interfaz para publicar experiencias de laboratorio en Canvas."""

import argparse

import Canvas_Lab as canvas_lab


def _usuarios_disponibles():
    return sorted(
        key for key in canvas_lab.USERS
        if not key.endswith("_id")
    )


def main():
    parser = argparse.ArgumentParser(
        description="Sube los documentos de una experiencia de laboratorio a Canvas."
    )
    parser.add_argument(
        "--experiencia",
        "--exp",
        dest="experiencia",
        type=int,
        required=True,
        help="Número de experiencia a subir. Ejemplo: --experiencia 1 o --exp 1.",
    )
    parser.add_argument(
        "--titulo-modulo",
        default=None,
        help="Nombre visible opcional del módulo en Canvas.",
    )
    parser.add_argument("--titulo-guia", default=None)
    parser.add_argument("--titulo-rubrica", default=None)
    parser.add_argument("--titulo-template", default=None)
    parser.add_argument(
        "--titulo-entrega",
        default=None,
        help=(
            "Nombre visible opcional de la tarea. "
            "Predeterminado: 'Entrega Experiencia XX'."
        ),
    )
    parser.add_argument(
        "--dias-entrega",
        type=int,
        default=14,
        help="Días desde la subida hasta el vencimiento (predeterminado: 14).",
    )
    parser.add_argument(
        "--hora-cierre",
        default="23:30",
        help="Hora local de cierre HH:MM (predeterminado: 23:30).",
    )
    parser.add_argument(
        "--puntos",
        type=float,
        default=7,
        help="Puntaje máximo de la entrega (predeterminado: 7).",
    )
    parser.add_argument(
        "--extensiones",
        default="pdf",
        help=(
            "Extensiones permitidas separadas por comas "
            "(predeterminado: pdf)."
        ),
    )
    parser.add_argument(
        "--intentos",
        type=int,
        default=2,
        help="Número de intentos permitidos (predeterminado: 2).",
    )
    parser.add_argument(
        "--usuarios",
        default="",
        help="Lista de usuarios separada por comas. Obligatoria salvo --todos.",
    )
    parser.add_argument(
        "--todos",
        action="store_true",
        help="Opera explícitamente sobre todos los usuarios de Key.txt.",
    )
    modo = parser.add_mutually_exclusive_group()
    modo.add_argument(
        "--test-mode",
        action="store_true",
        help="Modo de prueba sin publicar (comportamiento predeterminado).",
    )
    modo.add_argument(
        "--produccion",
        action="store_true",
        help="Publica el módulo, sus documentos y la tarea de entrega.",
    )
    args = parser.parse_args()

    if args.dias_entrega < 0:
        parser.error("--dias-entrega no puede ser negativo.")
    if args.puntos < 0:
        parser.error("--puntos no puede ser negativo.")
    if args.intentos < 1:
        parser.error("--intentos debe ser al menos 1.")

    try:
        hora, minuto = (int(value) for value in args.hora_cierre.split(":"))
        if not 0 <= hora <= 23 or not 0 <= minuto <= 59:
            raise ValueError
    except (TypeError, ValueError):
        parser.error("--hora-cierre debe usar el formato HH:MM.")

    extensiones = [
        value.strip().lower().lstrip(".")
        for value in args.extensiones.split(",")
        if value.strip()
    ]
    if not extensiones:
        parser.error("--extensiones debe contener al menos una extensión.")

    if args.usuarios and args.todos:
        parser.error("Usa --usuarios o --todos, no ambos.")
    if not args.usuarios and not args.todos:
        parser.error("Indica --usuarios NOMBRE[,NOMBRE] o usa --todos.")

    disponibles = _usuarios_disponibles()
    if not disponibles:
        print("❌ No hay usuarios configurados en Key.txt")
        return 1
    usuarios = (
        disponibles
        if args.todos
        else [value.strip() for value in args.usuarios.split(",") if value.strip()]
    )
    desconocidos = [usuario for usuario in usuarios if usuario not in disponibles]
    if desconocidos:
        print(f"❌ Usuarios no configurados: {', '.join(desconocidos)}")
        return 1

    titulos_documentos = {
        categoria: titulo
        for categoria, titulo in (
            ("guia", args.titulo_guia),
            ("rubrica", args.titulo_rubrica),
            ("template", args.titulo_template),
        )
        if titulo is not None
    }
    test_mode = not args.produccion
    errores = []

    for usuario in usuarios:
        print(f"\n--- Usuario: {usuario} ---")
        if not canvas_lab.select_user(usuario):
            errores.append((usuario, "No se pudo conectar"))
            continue
        resultado = canvas_lab.subir_experiencia(
            args.experiencia,
            test_mode=test_mode,
            titulo_modulo=args.titulo_modulo,
            titulos_documentos=titulos_documentos,
            titulo_entrega=args.titulo_entrega,
            dias_entrega=args.dias_entrega,
            hora_cierre=(hora, minuto),
            puntos_entrega=args.puntos,
            extensiones_entrega=extensiones,
            intentos_entrega=args.intentos,
        )
        if resultado is None:
            errores.append((usuario, "No se pudo subir la experiencia"))

    print("\n" + "=" * 80)
    print(f"Exitosos: {len(usuarios) - len(errores)}")
    print(f"Con error: {len(errores)}")
    for usuario, motivo in errores:
        print(f"  - {usuario}: {motivo}")
    return 0 if not errores else 1


if __name__ == "__main__":
    raise SystemExit(main())
