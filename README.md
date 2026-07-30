# Física Aplicada a las Ciencias Farmacéuticas

Este repositorio organiza el material de trabajo para el curso **DFFR300 - Física Aplicada a las Ciencias Farmacéuticas**. Su propósito es reunir, ordenar y desarrollar materiales docentes para clases teóricas, actividades de laboratorio y planificación general del curso.

El curso está pensado para estudiantes de primer año del área química y farmacéutica. Por eso, el material debe mantener un equilibrio claro: suficiente rigor físico para formar criterio, pero con un lenguaje accesible, ejemplos guiados y énfasis en aplicaciones medibles o interpretables dentro de sistemas químicos, biológicos y farmacéuticos.

## Objetivo del repositorio

La meta es construir un conjunto coherente de materiales que permitan:

- desarrollar las clases conforme a la distribución oficial semana a semana;
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

La prioridad de las fuentes es:

1. `Syllabus-DFBR300-202620_v0.docx`: ley del curso para aprendizajes
   esperados, contenidos, alcance y evaluación.
2. `WEEK2WEEK-DISTRIBUTIONLAB-v1-DFFR300 .pdf`: distribución vigente de esos
   contenidos por semana. Ordena el trabajo, pero no puede agregar, quitar ni
   contradecir contenidos del syllabus.
3. Los libros de `general/`: fuentes para explicar, derivar, ejemplificar y
   construir la pizarra. `Serway_vol1-7Ed.pdf` aporta la base física general y
   `martins-2011.pdf` fundamenta los ejemplos cualitativos químicos y
   farmacéuticos de los bloques morados.
4. `1Clases.pdf`: antecedente visual y pedagógico complementario; no reemplaza
   las fuentes anteriores.

No debe mantenerse una planificación paralela dentro de `lectures/`. Si
aparece una diferencia entre documentos, prevalece siempre el syllabus.

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
    build/
    tmp/
```

Cada parte semanal debe dejar claro:

- qué contenido del syllabus cubre;
- qué secciones del texto base usa;
- de dónde viene la clase anterior;
- hacia qué idea prepara la clase siguiente;
- qué definiciones, ecuaciones y ejemplos deberían quedar en el cuaderno del estudiante.

La trazabilidad bibliográfica se mantiene de forma centralizada y breve en
`lectures/BITACORA.md`. No se crean archivos `cobertura.txt` por semana.
Las reglas reproducibles para construir y revisar los apuntes están en
`lectures/INSTRUCCIONES.md`.

## `lab/`

Contiene el diseño del laboratorio del curso.

El laboratorio debe conectar la física básica con mediciones reales, uso de
instrumentos, análisis de datos y discusión de errores. La organización
recomendada es por experiencias oficiales, no por semanas.

Estructura sugerida:

```text
lab/
  INSTRUCCIONES.md
  BITACORA.md
  ejemplos/
  slides_exp01/
    presentacion.tex
    Makefile
    assets/
  experiencia01-nombre-breve/
    README.md
    guia/
    rubrica/
    template/
    instrumentos/
    datos/
    guia-docente.md
```

El syllabus también es la autoridad para el laboratorio. La sesión semanal
tiene 2 horas pedagógicas y el trabajo experimental se realiza en grupos de
cuatro. Las presentaciones Beamer se guardan separadamente en
`lab/slides_expXX/`; el flujo de Canvas publica solo la guía, la rúbrica y el
template de cada `experienciaXX-*`.

Cada experiencia debería partir de una pregunta clara:

- ¿Qué se quiere medir?
- ¿Qué fenómeno físico está involucrado?
- ¿Qué instrumentos se necesitan?
- ¿Qué datos se registran?
- ¿Cómo se analizan?
- ¿Qué conclusión puede defenderse con evidencia?

El archivo `lab/README.md` presenta la organización general de estas
experiencias. `lab/INSTRUCCIONES.md` contiene el procedimiento reproducible y
`lab/BITACORA.md` registra fuentes, estado y cambios de cada experiencia.

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

1. Determinar en el syllabus los aprendizajes y contenidos permitidos.
2. Ubicar la semana en `WEEK2WEEK-DISTRIBUTIONLAB-v1-DFFR300 .pdf`.
3. Seleccionar capítulos y páginas de los libros de `general/`.
4. Construir el desarrollo físico desde los textos base.
5. Preparar con `martins-2011.pdf` al menos un puente químico o farmacéutico
   pertinente cuando el tema lo permita, presentado en un bloque morado.
6. Desarrollar el artículo de pizarra y compilarlo.
7. Verificar que el PDF no exceda ni omita el alcance del syllabus.
8. Actualizar `lectures/BITACORA.md` con tema, estado y páginas realmente
   utilizadas.

Para desarrollar un laboratorio:

1. Revisar en el syllabus la unidad, el aprendizaje, la evaluación y las
   reglas aplicables.
2. Definir la pregunta experimental.
3. Confirmar la ubicación en el documento semana a semana.
4. Revisar instrumentos disponibles.
5. Diseñar procedimiento y registro de datos para una sesión de 2 horas
   pedagógicas y grupos de cuatro.
6. Probar si los datos son razonables.
7. Escribir guía de estudiante, guía docente, template y rúbrica.
8. Preparar en `lab/slides_expXX/` las slides breves para abrir la sesión; no
   se publican en Canvas por el momento.

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
- una distribución oficial semana a semana;
- criterios para escribir clases teóricas;
- una guía inicial para diseñar el laboratorio.

Los próximos pasos naturales son crear las carpetas de semanas en `lectures/`,
definir las primeras experiencias en `lab/` y completar la fuente base para
electricidad y magnetismo.
