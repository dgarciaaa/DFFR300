# Física Aplicada a las Ciencias Farmacéuticas

Este repositorio organiza el material de trabajo para el curso **DFFR300 - Física Aplicada a las Ciencias Farmacéuticas**. Su propósito es reunir, ordenar y desarrollar materiales docentes para clases teóricas, actividades de laboratorio y planificación general del curso.

El curso está pensado para estudiantes de primer año del área química y farmacéutica. Por eso, el material debe mantener un equilibrio claro: suficiente rigor físico para formar criterio, pero con un lenguaje accesible, ejemplos guiados y énfasis en aplicaciones medibles o interpretables dentro de sistemas químicos, biológicos y farmacéuticos.

## Objetivo del repositorio

La meta es construir un conjunto coherente de materiales que permitan:

- planificar el curso semana a semana;
- escribir apuntes breves para clases de pizarra;
- preparar actividades de laboratorio conectadas con la teoría;
- conservar las fuentes base y documentos oficiales;
- dejar trazabilidad de decisiones, avances y versiones mediante Git.

El repositorio no busca ser solo una carpeta de archivos. Debe funcionar como un espacio de producción docente: cada material debería explicar qué problema aborda, con qué fuente se construye, cómo se conecta con el curso y qué se espera que el estudiante aprenda.

## Estructura general

```text
.
├── general/
├── lectures/
├── lab/
└── README.md
```

## `general/`

Contiene documentos de referencia para construir el curso:

- syllabus o programa oficial;
- textos base;
- presentaciones o materiales heredados;
- documentos de apoyo para planificación.

Estos archivos no son materiales finales para estudiantes necesariamente. Funcionan como fuentes para tomar decisiones sobre contenidos, profundidad, secuencia y resultados de aprendizaje.

Fuentes actuales relevantes:

- `DFFR300_Física Aplicada a las Ciencias Farmacéuticas.pdf`: programa oficial del curso.
- `Serway_vol1-7Ed.pdf`: texto base principal para mecánica, fluidos y termodinámica.
- `1Clases.pdf`: apoyo visual y referencia pedagógica previa.

Para la unidad de electricidad y magnetismo conviene incorporar una fuente de física general equivalente a Serway Vol. 2. Textos más avanzados, como Griffiths, pueden servir como referencia docente puntual, pero no como base directa para estudiantes de primer año.

## `lectures/`

Contiene la planificación y el desarrollo de las clases teóricas.

La idea central es producir apuntes semanales en formato de artículo breve, pensados como guía para clase de pizarra. Estos apuntes no reemplazan una presentación visual: fijan la secuencia conceptual, las definiciones, las ecuaciones mínimas, los ejemplos resueltos y los ejercicios de cierre.

Cada semana debería organizarse en una carpeta independiente:

```text
lectures/
  semana01/
    Makefile
    preamble.tex
    semana01-P1.tex
    semana01-P2.tex
    cobertura.txt
    build/
    tmp/
```

Cada parte semanal debe dejar claro:

- qué contenido del syllabus cubre;
- qué secciones del texto base usa;
- de dónde viene la clase anterior;
- hacia qué idea prepara la clase siguiente;
- qué definiciones, ecuaciones y ejemplos deberían quedar en el cuaderno del estudiante.

El archivo `lectures/plan_semanal_curso.txt` contiene una planificación tentativa de 16 semanas, con dos clases semanales, organizada por unidades:

- Unidad I: mecánica de la partícula en una dimensión;
- Unidad II: mecánica de fluidos;
- Unidad III: temperatura, calor y termodinámica;
- Unidad IV: electricidad y magnetismo.

## `lab/`

Contiene el diseño del laboratorio del curso.

El laboratorio debe conectar la física básica con mediciones reales, uso de instrumentos, análisis de datos y discusión de errores. La organización recomendada es por experimentos, no estrictamente por semanas, porque una experiencia puede ocupar una o más sesiones.

Estructura sugerida:

```text
lab/
  experimento01-nombre-breve/
    README.md
    slides/
    instrumentos/
    datos/
    guia-estudiante.md
    guia-docente.md
    rubrica.md
```

Cada experimento debería partir de una pregunta clara:

- ¿Qué se quiere medir?
- ¿Qué fenómeno físico está involucrado?
- ¿Qué instrumentos se necesitan?
- ¿Qué datos se registran?
- ¿Cómo se analizan?
- ¿Qué conclusión puede defenderse con evidencia?

El archivo `lab/idea.md` fija los criterios generales para construir estas experiencias.

## Criterio pedagógico

El curso debe construir una historia progresiva. No basta con listar fórmulas: cada tema debe aparecer como respuesta a una necesidad física concreta.

Al escribir materiales, conviene mantener estos criterios:

- usar lenguaje directo y comprensible;
- introducir las ecuaciones desde el fenómeno, no como recetas aisladas;
- cuidar unidades, dimensiones, signos y supuestos;
- cerrar cada clase o experiencia con una tarea operativa;
- conectar teoría, laboratorio y aplicaciones;
- evitar profundidad matemática que no aporte al objetivo del curso.

La referencia conceptual principal debe ser física general universitaria. El nivel esperado no es el de un curso formal para físicos, sino el de una formación aplicada para ciencias farmacéuticas.

## Flujo de trabajo sugerido

Para desarrollar una clase:

1. Revisar el contenido correspondiente en el syllabus.
2. Ubicar las secciones del texto base.
3. Mirar el plan semanal para mantener continuidad.
4. Escribir el propósito de la clase.
5. Definir las fuentes usadas.
6. Desarrollar el guion conceptual.
7. Agregar ejemplos mínimos y ejercicios de cierre.
8. Registrar en `cobertura.txt` qué quedó cubierto y qué queda pendiente.

Para desarrollar un laboratorio:

1. Definir la pregunta experimental.
2. Identificar la unidad del curso que refuerza.
3. Revisar instrumentos disponibles.
4. Diseñar procedimiento y registro de datos.
5. Probar si los datos son razonables.
6. Escribir guía de estudiante, guía docente y rúbrica.
7. Preparar slides breves para abrir la sesión.

## Uso de Git

Este repositorio está pensado para versionar el desarrollo del curso. Un ciclo simple de trabajo es:

```bash
git status
git add .
git commit -m "Describe el cambio"
git push
```

Para revisar el historial:

```bash
git log --oneline
```

Como el proyecto puede contener PDFs grandes, conviene cuidar qué archivos se suben. GitHub recomienda usar Git LFS para archivos pesados, especialmente sobre 50 MB.

## Estado actual

El proyecto está en etapa de organización inicial. Ya existen:

- fuentes generales del curso;
- una planificación semanal tentativa;
- criterios para escribir clases teóricas;
- una guía inicial para diseñar el laboratorio.

Los próximos pasos naturales son crear las carpetas de semanas en `lectures/`, definir los primeros experimentos en `lab/` y completar la fuente base para electricidad y magnetismo.
