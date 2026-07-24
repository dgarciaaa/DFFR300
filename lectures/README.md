# Clases teóricas

Esta carpeta reúne los apuntes de las clases teóricas de **DFFR300 — Física
Aplicada a las Ciencias Farmacéuticas**.

## Organización

```text
lectures/
├── plan_semanal_curso.txt
├── semana01/
│   ├── semana01-P1.pdf
│   ├── semana01-P2.pdf
│   ├── semana01-P1.tex
│   ├── semana01-P2.tex
│   ├── preamble.tex
│   ├── cobertura.txt
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
- `cobertura.txt`: contenidos y referencias utilizados.
- `Makefile`: comandos de compilación y limpieza.

El archivo `plan_semanal_curso.txt` presenta la secuencia general de contenidos
del semestre.

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
