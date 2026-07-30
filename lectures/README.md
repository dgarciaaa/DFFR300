# Clases teóricas

Esta carpeta reúne los apuntes de las clases teóricas de **DFFR300 — Física
Aplicada a las Ciencias Farmacéuticas**.

## Organización

```text
lectures/
├── BITACORA.md
├── INSTRUCCIONES.md
├── semana01/
│   ├── semana01-P1.pdf
│   ├── semana01-P2.pdf
│   ├── semana01-P1.tex
│   ├── semana01-P2.tex
│   ├── preamble.tex
│   └── Makefile
├── semana02/
│   └── …
└── semanaXX/
    └── …
```

Cada carpeta semanal contiene dos partes:

- `semanaXX-P1.pdf`: primera clase de la semana.
- `semanaXX-P2.pdf`: segunda clase de la semana.
- `semanaXX-P1.tex` y `semanaXX-P2.tex`: archivos fuente en LaTeX.
- `preamble.tex`: configuración y estilo compartidos por ambas partes.
- `Makefile`: comandos de compilación y limpieza.

La secuencia del semestre proviene de
`general/WEEK2WEEK-DISTRIBUTIONLAB-v1-DFFR300 .pdf`, subordinada siempre al
syllabus `general/Syllabus-DFBR300-202620_v0.docx`.

`BITACORA.md` registra de manera breve qué se está viendo, el estado de cada
parte y las páginas de los textos realmente utilizadas. Debe actualizarse cada
vez que cambie un archivo de `lectures/`. No reemplaza el syllabus ni el
documento semana a semana.

`INSTRUCCIONES.md` contiene el procedimiento completo y los criterios de
contenido, escritura, bloques de color, compilación y revisión. Forma parte del
repositorio para que otra persona o una nueva sesión de Codex pueda reproducir
el mismo flujo.

## Fuentes

El contenido y su profundidad se deciden en este orden:

1. syllabus;
2. distribución oficial semana a semana;
3. libros de `general/`;
4. materiales complementarios.

La física se desarrolla desde los textos generales. El enfoque químico y
farmacéutico se presenta en los bloques morados y debe fundamentarse
preferentemente en `general/martins-2011.pdf`. Toda fuente usada debe quedar
identificada por capítulo o sección y páginas en `BITACORA.md`.

## Compilación

Desde la carpeta de una semana:

```bash
make pdf
```

Para eliminar los archivos auxiliares:

```bash
make clean
```

Los PDF terminados permanecen en la carpeta de la semana.
