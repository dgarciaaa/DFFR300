# Lectures del curso

Esta carpeta organiza los escritos semanales para el curso **Fisica Aplicada a las Ciencias Farmaceuticas**.

Cada semana debe vivir en una carpeta independiente:

```text
lectures/
  semana01/
    Makefile
    preamble.tex
    semana01-P1.tex
    semana01-P2.tex
    semana01-P1.pdf
    semana01-P2.pdf
    cobertura.txt
    build/
    tmp/
```

La idea es que cada `semanaXX-P*.tex` sea un articulo breve y limpio, pensado como base para escribir en pizarra. No reemplaza a las diapositivas: las diapositivas sirven como apoyo visual, mientras que el escrito fija la secuencia conceptual, las definiciones, los ejemplos y los ejercicios minimos.

## Convencion sugerida

- `preamble.tex`: paquetes, macros y estilo local de la semana.
- `semanaXX-P1.tex`: documento de la primera clase semanal.
- `semanaXX-P2.tex`: documento de la segunda clase semanal.
- `Makefile`: compila el PDF de la semana con `make pdf`.
- `cobertura.txt`: resumen de contenidos cubiertos, fuentes usadas y puente con la semana siguiente.
- `build/`: carpeta generada por LaTeX para archivos auxiliares.
- `tmp/`: temporales de revision o renderizado asociados solo a esa semana.

Los temporales de una semana deben quedar dentro de su propia carpeta `semanaXX/`. No se deben crear carpetas `tmp/` en la raiz del curso para artefactos de una semana.

## Fuentes base

Las semanas se deben construir cruzando:

- `general/DFFR300_Fisica Aplicada a las Ciencias Farmaceuticas.pdf`: resultados de aprendizaje y contenidos oficiales.
- `general/Serway_vol1-7Ed.pdf`: desarrollo conceptual de referencia.
- `general/1Clases.pdf`: apoyo visual y orden pedagogico ya existente.

## Compilacion

Desde una carpeta semanal:

```bash
make pdf
```

Esto compila todos los documentos `semanaXX-P*.tex` de esa semana.

Para limpiar auxiliares:

```bash
make clean
```

## Criterio de escritura

El texto debe mantenerse en formato de articulo, con secciones breves y ejemplos resueltos. Conviene terminar cada parte con una lista corta de ejercicios de pizarra o discusion para que la clase tenga cierre operativo.

El texto debe explicitar lo que conviene escribir en pizarra: definiciones en orden, ecuaciones minimas, tablas de signos, rutinas de resolucion y frases de cierre conceptual. La explicacion puede ser narrativa, pero debe dejar claro que material deberia quedar en los cuadernos de los estudiantes.

Cada `.tex` debe incluir, inmediatamente despues de `Proposito`, una seccion `Fuentes usadas`. Esa seccion debe mencionar:

- La unidad y contenidos del syllabus que se estan cubriendo.
- El libro base usado, indicando explicitamente capitulo, titulo y secciones usadas.
- La presentacion u otro material de apoyo usado.

Cuando se use Serway, no basta con escribir solo el capitulo; se deben listar las secciones concretas, por ejemplo: `1.1 Estandares de longitud, masa y tiempo`, `1.3 Analisis dimensional`, etc.

## Estilo docente

Cada apunte debe estar escrito como un guion riguroso para pizarra. La base conceptual debe ser el libro, siguiendo su desarrollo en orden natural, pero el texto no debe copiarlo: debe reformular, ampliar y explicar como lo haria un profesor frente al curso.

La escritura debe construir una historia semana a semana. Cada clase debe dejar claro:

- De donde viene el tema y hacia donde prepara la clase siguiente.
- Que problema fisico o necesidad conceptual motiva cada definicion.
- Que se debe escribir en pizarra y en que orden conviene desarrollarlo.
- Como se conectan las ecuaciones con unidades, dimensiones, signos y supuestos.
- Que ejemplos minimos permiten cerrar la idea antes de pasar al tema siguiente.

Como regla practica, cada parte semanal debe mantenerse en torno a 10 paginas como maximo. Si el desarrollo supera ese tamano, se debe dividir mejor el contenido o mover detalles secundarios a ejercicios.
