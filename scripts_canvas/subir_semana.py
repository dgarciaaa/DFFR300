#!/usr/bin/env python3
import argparse
import sys

import Canvas_Key as ck


def _usuarios_disponibles():
    return sorted([k for k in ck.USERS.keys() if not k.endswith("_id")])


def _parsear_usuarios(raw, disponibles):
    if not raw:
        return disponibles
    pedidos = [u.strip() for u in raw.split(",") if u.strip()]
    return pedidos


def main():
    parser = argparse.ArgumentParser(
        description="Sube una semana a Canvas para múltiples usuarios."
    )
    parser.add_argument("--semana", type=int, default=None, help="Semana a subir (1-16).")
    parser.add_argument(
        "--titulo-semana",
        type=str,
        default=None,
        help="Título visible opcional del encabezado semanal en Canvas.",
    )
    parser.add_argument(
        "--titulo-p1",
        type=str,
        default=None,
        help="Título visible opcional del PDF P1 en Canvas.",
    )
    parser.add_argument(
        "--titulo-p2",
        type=str,
        default=None,
        help="Título visible opcional del PDF P2 en Canvas.",
    )
    parser.add_argument(
        "--usuarios",
        type=str,
        default="",
        help="Lista separada por coma. Es obligatoria salvo que se use --todos.",
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
        help="Usa el módulo TEST y no publica (valor predeterminado).",
    )
    modo.add_argument(
        "--produccion",
        action="store_true",
        help="Opera sobre el módulo real y publica. Debe indicarse explícitamente.",
    )
    parser.add_argument(
        "--eliminar-semana",
        type=int,
        default=None,
        help="Elimina esta semana del módulo. Puede usarse sola o junto a --semana. "
             "Ej: --eliminar-semana 13 --semana 12.",
    )

    args = parser.parse_args()

    if args.semana is None and args.eliminar_semana is None:
        parser.error("Debes indicar --semana, --eliminar-semana, o ambos.")
    if args.semana is None and any((args.titulo_semana, args.titulo_p1, args.titulo_p2)):
        parser.error("Los títulos personalizados requieren indicar --semana.")
    if args.usuarios and args.todos:
        parser.error("Usa --usuarios o --todos, no ambos.")
    if not args.usuarios and not args.todos:
        parser.error("Indica --usuarios NOMBRE[,NOMBRE] o usa --todos explícitamente.")

    disponibles = _usuarios_disponibles()
    if not disponibles:
        print("❌ No hay usuarios configurados en Key.txt")
        return 1

    usuarios = disponibles if args.todos else _parsear_usuarios(args.usuarios, disponibles)
    test_mode = not args.produccion
    desconocidos = [u for u in usuarios if u not in disponibles]
    if desconocidos:
        print(f"❌ Usuarios no encontrados en Key.txt: {', '.join(desconocidos)}")
        print(f"💡 Disponibles: {', '.join(disponibles)}")
        return 1

    print("=" * 80)
    if args.semana is not None and args.eliminar_semana is not None:
        print("🗑️📤 ELIMINACIÓN Y SUBIDA MASIVA DE SEMANA")
    elif args.semana is not None:
        print("📤 SUBIDA MASIVA DE SEMANA")
    else:
        print("🗑️ ELIMINACIÓN MASIVA DE SEMANA")
    if args.semana is not None:
        print(f"Semana a subir: {args.semana}")
    if args.eliminar_semana is not None:
        print(f"Semana a eliminar: {args.eliminar_semana}")
    print(f"Usuarios: {', '.join(usuarios)}")
    print(f"Modo: {'TEST (no publica)' if test_mode else 'PRODUCCIÓN (publica)'}")
    print("=" * 80)

    errores = []
    exitos = []

    for usuario in usuarios:
        print(f"\n--- Usuario: {usuario} ---")

        if not ck.select_user(usuario):
            errores.append((usuario, "No se pudo conectar"))
            continue

        if args.eliminar_semana is not None:
            eliminado = ck.eliminar_semana(
                args.eliminar_semana,
                test_mode=test_mode,
            )
            if eliminado is None:
                errores.append((usuario, f"Fallo en eliminar_semana({args.eliminar_semana})"))
                continue

        if args.semana is not None:
            titulos_pdf = {
                parte: titulo
                for parte, titulo in (("P1", args.titulo_p1), ("P2", args.titulo_p2))
                if titulo is not None
            }
            resultado = ck.subir_contenido(
                args.semana,
                test_mode=test_mode,
                titulo_semana=args.titulo_semana,
                titulos_pdf=titulos_pdf,
            )
            if resultado is None:
                errores.append((usuario, "Fallo en subir_contenido"))
            else:
                exitos.append(usuario)
        else:
            exitos.append(usuario)

    print("\n" + "=" * 80)
    print("RESUMEN")
    print(f"✅ Exitosos: {len(exitos)}")
    if exitos:
        print(f"   {', '.join(exitos)}")
    print(f"❌ Con error: {len(errores)}")
    for usuario, motivo in errores:
        print(f"   - {usuario}: {motivo}")
    print("=" * 80)

    return 0 if not errores else 1


if __name__ == "__main__":
    raise SystemExit(main())
