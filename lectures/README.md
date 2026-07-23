# Apuntes de pizarra del curso

Esta carpeta contiene los apuntes de pizarra para el curso **Física Aplicada a
las Ciencias Farmacéuticas**.

Cada archivo `semanaXX-P*.tex` debe producir un artículo completo que contenga,
en el orden correcto, todo lo que se desarrollará en la pizarra durante una
clase. El documento no es una pauta para el docente, una planificación de
actividades ni un resumen posterior de la materia:

> **El artículo es la pizarra.**

El docente debe poder seguir el documento desde el inicio hasta el final y
trasladar su desarrollo a la pizarra: títulos, definiciones, explicaciones,
dibujos, ecuaciones, derivaciones, ejemplos, interpretaciones y conclusiones.

## Organización de archivos

Cada semana vive en una carpeta independiente:

```text
lectures/
  semanaXX/
    Makefile
    preamble.tex
    semanaXX-P1.tex
    semanaXX-P2.tex
    semanaXX-P1.pdf
    semanaXX-P2.pdf
    cobertura.txt
    build/
    tmp/
```

- `semanaXX-P1.tex`: apunte de pizarra de la primera clase semanal.
- `semanaXX-P2.tex`: apunte de pizarra de la segunda clase semanal.
- `preamble.tex`: paquetes, macros y estilo visual de la semana.
- `Makefile`: compilación de todos los documentos de la semana.
- `cobertura.txt`: relación entre syllabus, bibliografía y contenidos.
- `build/`: archivos auxiliares generados por LaTeX.
- `tmp/`: archivos temporales de revisión de esa semana.

Las fuentes, capítulos y secciones utilizadas se registran en
`cobertura.txt`. No deben ocupar páginas dentro del apunte.

## Fuentes para construir los apuntes

Cada clase debe prepararse cruzando:

- `general/DFFR300_Fisica Aplicada a las Ciencias Farmaceuticas.pdf`: resultados
  de aprendizaje y contenidos oficiales.
- `general/Serway_vol1-7Ed.pdf`: desarrollo conceptual para mecánica, fluidos y
  termodinámica.
- `general/1Clases.pdf`: apoyo visual y antecedente del orden pedagógico.
- `lectures/plan_semanal_curso.txt`: continuidad entre las clases del semestre.
- `cobertura.txt` de la semana: contenidos y secciones bibliográficas que deben
  cubrirse.

Para electricidad y magnetismo debe incorporarse una fuente base equivalente
al volumen 2 de Serway. Griffiths puede servir como referencia puntual para el
docente, pero no debe determinar el nivel matemático ni la profundidad del
apunte.

Las fuentes no se copian. Se estudian, se cruzan y se reformulan para construir
una exposición propia, coherente y adecuada al curso.

## Estructura obligatoria del PDF

### Página 1: portada

La portada debe ocupar una sola página y contener:

- nombre del curso;
- semana y parte;
- título específico de la clase;
- texto `Profesor: Diego García`;
- fecha o semestre solamente cuando corresponda.

La portada debe ser limpia y sobria. No debe incluir objetivos, resúmenes,
fuentes ni texto introductorio.

### Página 2: índice

El índice debe ocupar la segunda página. Debe mostrar las secciones y
subsecciones del desarrollo para que el apunte pueda recorrerse rápidamente.

La portada y el índice no cuentan como páginas de contenido.

### Desde la página 3: contenido de pizarra

Después del índice debe comenzar inmediatamente la materia. En este punto se
reinicia la numeración de páginas en `1`, de modo que la numeración visible
corresponda solo al contenido efectivo.

No se deben agregar antes del contenido secciones como:

- Propósito;
- Fuentes usadas;
- Preparación docente;
- Resultados mínimos;
- Objetivos de la clase;
- Recomendaciones para el profesor;
- Materiales necesarios;
- instrucciones sobre qué decir o cuándo hacer una pausa.

Toda información bibliográfica pertenece a `cobertura.txt`.

## Mapa inicial de contenidos

La primera sección del contenido debe presentar un mapa conceptual breve de la
clase. Este mapa no es una distribución de minutos ni una pauta de acciones
docentes. Su función es mostrar el hilo físico que se construirá.

Siempre que sea posible debe escribirse como una cadena lineal de flechas. Por
ejemplo:

```latex
\[
  \text{posición}
  \longrightarrow
  \text{desplazamiento}
  \longrightarrow
  \text{velocidad}
  \longrightarrow
  \text{aceleración}.
\]
```

Si el tema no admite una cadena lineal, puede usarse un esquema pequeño con
ramificaciones. El mapa debe contener conceptos físicos, no acciones como
`explicar`, `preguntar`, `resolver` o `cerrar`.

## El artículo es la pizarra

El cuerpo del documento debe escribirse como un artículo continuo y ordenado.
Cada párrafo tiene que corresponder a una explicación que vale la pena
construir o dejar anotada en la pizarra. No se incluyen instrucciones internas
como:

- `el docente debe decir`;
- `conviene dibujar`;
- `preguntar al curso`;
- `escribir en la pizarra`;
- `hacer una pausa`;
- `si queda tiempo`.

En su lugar, debe aparecer directamente el contenido. Si se necesita un eje,
un gráfico, una tabla, un diagrama de cuerpo libre o un esquema, el dibujo debe
formar parte del artículo. Si se necesita una frase de interpretación, esa
frase se escribe directamente.

Ejemplo incorrecto:

```text
Conviene dibujar una curva posición-tiempo y explicar que su pendiente
representa la velocidad.
```

Ejemplo correcto:

```latex
\[
  \text{pendiente de la gráfica }x(t)
  =
  \frac{\Delta x}{\Delta t}
  =
  v_{x,\mathrm{med}}.
\]

La pendiente de una gráfica posición-tiempo mide el cambio de posición por
unidad de tiempo. Una pendiente positiva representa movimiento hacia \(+x\);
una pendiente negativa representa movimiento hacia \(-x\).
```

El texto puede tener un tono cercano y cotidiano. Debe sonar como una buena
explicación de cátedra, no como un reglamento ni como la copia literal de un
libro. La precisión física y matemática se mantiene, pero las ideas pueden
explicarse con frases naturales, comparaciones sencillas y preguntas que
ayuden a pensar.

## Orden del desarrollo

Cada clase debe construir una historia física. El orden general es:

1. mapa conceptual del contenido;
2. situación o problema físico que da origen al tema;
3. conceptos y definiciones necesarios;
4. representación mediante dibujos, tablas o gráficos;
5. desarrollo matemático y derivaciones;
6. interpretación física de los resultados;
7. ejemplos resueltos;
8. relaciones con contenidos anteriores o posteriores;
9. síntesis final.

Esta secuencia no se presenta como una lista de instrucciones dentro del PDF.
Se manifiesta directamente en el orden de las secciones del artículo.

## Definiciones

Toda definición importante debe incluir:

- la necesidad física que la hace aparecer;
- su formulación en palabras;
- su expresión matemática, cuando corresponda;
- el significado de cada símbolo;
- sus unidades;
- el papel del signo o de la dirección;
- una interpretación sencilla;
- la diferencia con conceptos cercanos que suelen confundirse.

Por ejemplo, no basta con escribir

```latex
\[
  v_{x,\mathrm{med}}=\frac{\Delta x}{\Delta t}.
\]
```

También debe quedar claro que utiliza desplazamiento, que conserva el signo,
que describe un intervalo y que no es lo mismo que rapidez media.

## Leyes, modelos y supuestos

Las leyes físicas deben presentarse indicando qué relación expresan y en qué
tipo de situación pueden utilizarse.

Los modelos deben declarar sus supuestos antes de aplicar una ecuación. Por
ejemplo:

- partícula;
- movimiento en una dimensión;
- aceleración constante;
- fluido ideal e incompresible;
- equilibrio térmico;
- resistencia óhmica;
- campo uniforme.

Una ecuación no debe aparecer como receta aislada. El artículo debe dejar claro
de dónde viene, qué significa y cuándo deja de ser válida.

## Derivaciones

Las derivaciones importantes para el nivel del curso deben desarrollarse
completas y en el mismo orden en que se escribirían en la pizarra:

1. definición, ley o ecuación de partida;
2. supuestos utilizados;
3. pasos algebraicos intermedios;
4. resultado final;
5. revisión de unidades o dimensiones;
6. interpretación física.

No se debe usar una frase como `de aquí se obtiene` para ocultar el paso que
contiene la idea central. Tampoco es necesario llenar el apunte con álgebra
repetitiva que no agregue comprensión.

Debe distinguirse entre:

- una **definición**, que se establece y se interpreta;
- una **ley física**, que expresa una regularidad de la naturaleza;
- una **ecuación derivada**, que se obtiene a partir de definiciones, leyes y
  supuestos.

## Dibujos, gráficos y esquemas

Todo dibujo necesario para comprender el desarrollo debe estar incorporado en
el documento, no descrito como una tarea futura.

Los gráficos deben incluir:

- ejes y sentido positivo;
- variable y unidad de cada eje;
- puntos, pendientes o áreas relevantes;
- signos y regiones necesarias para la interpretación.

Los diagramas físicos deben incluir las etiquetas indispensables y mantener un
estilo sencillo que pueda reproducirse a mano en la pizarra. No se buscan
ilustraciones decorativas ni diagramas demasiado elaborados.

Cuando la idea se entienda mejor mediante una secuencia lineal, debe escribirse
explícitamente con flechas. Por ejemplo:

```latex
\[
  \text{fuerza neta}
  \longrightarrow
  \text{aceleración}
  \longrightarrow
  \text{cambio de velocidad}
  \longrightarrow
  \text{cambio de posición}.
\]
```

## Ejemplos resueltos

Los ejemplos numéricos forman parte del contenido de pizarra y deben quedar
resueltos completamente. El desarrollo debe incluir, de manera natural:

- situación física;
- dibujo o representación;
- datos e incógnita;
- modelo y supuestos;
- ecuaciones utilizadas;
- desarrollo simbólico;
- sustitución con unidades;
- resultado;
- interpretación y revisión de si el valor es razonable.

No es necesario colocar estas etapas como instrucciones o casillas. Deben
verse directamente en la solución.

Los ejemplos deben corresponder al nivel del curso. Se prefieren situaciones
químicas, biológicas o farmacéuticas cuando ayudan realmente a comprender la
física. No se debe forzar el contexto si un carrito, una pelota, una caja o una
columna de agua muestran mejor la idea.

## Los dos únicos bloques de color

El diseño general debe ser limpio, sobrio y parecido a un artículo. No se deben
crear cajas de colores para definiciones, advertencias, resultados, objetivos,
instrucciones o conclusiones.

Solamente se permiten dos tipos de bloques de color.

### Bloque morado pastel: ejemplo cualitativo

Se utiliza para presentar una situación intuitiva relacionada con la sección
que acaba de desarrollarse. Puede incluir un dibujo sencillo, un esquema o una
comparación cotidiana.

Su función es ayudar a visualizar la idea antes o después del desarrollo
matemático. No reemplaza una definición, una derivación ni un ejemplo numérico
completo.

El título debe ser breve, por ejemplo:

```text
Ejemplo cualitativo: una gota que cae en un fluido
```

### Bloque azul pastel: pregunta

Se utiliza para dejar una pregunta conceptual que obligue a interpretar el
contenido de la sección.

La pregunta debe poder discutirse utilizando solamente lo que ya aparece en el
artículo. No debe introducir materia nueva ni funcionar como instrucción para
el docente.

El título debe ser simplemente:

```text
Pregunta
```

Estos bloques deben usarse con moderación. No es obligatorio colocar ambos en
cada sección ni llenar cada página con cajas. Deben aparecer solamente cuando
aclaran o profundizan una idea.

Los colores deben ser suaves:

- morado pastel para el ejemplo cualitativo;
- azul pastel para la pregunta;
- texto oscuro con contraste suficiente;
- bordes discretos y sin decoración excesiva.

## Síntesis final

La última sección debe cerrar el hilo conceptual de la clase. Debe contener una
síntesis breve de las relaciones más importantes, preferentemente mediante
ecuaciones, una tabla pequeña o una cadena de flechas.

No debe incluir comentarios sobre la planificación docente. El cierre también
es contenido de pizarra.

Cuando corresponda, la última relación puede preparar naturalmente el tema
siguiente. Por ejemplo:

```latex
\[
  \text{describir el movimiento}
  \longrightarrow
  \text{preguntar por su causa}
  \longrightarrow
  \text{introducir la fuerza}.
\]
```

## Extensión

La portada y el índice ocupan las primeras dos páginas y no cuentan como
contenido.

El contenido comienza en la tercera página del PDF, pero su numeración visible
se reinicia en `1`. A partir de allí, unas diez páginas constituyen una
referencia práctica, no un límite estricto.

El apunte puede superar diez páginas cuando las definiciones, derivaciones,
dibujos y ejemplos necesarios lo requieran. También puede ser más breve si el
tema queda completo. La prioridad es que la pizarra esté bien construida y no
que el documento alcance una cantidad fija de páginas.

No se debe eliminar una explicación necesaria, comprimir la tipografía ni
omitir pasos importantes para respetar un máximo artificial.

## Nivel y tono

El apunte debe ser riguroso y completo, pero no necesita sonar excesivamente
formal.

- Usar frases claras y naturales.
- Explicar primero la idea física y luego formalizarla.
- Introducir las ecuaciones como respuesta a una necesidad.
- Usar comparaciones cotidianas cuando aclaren el concepto.
- Evitar definiciones circulares y lenguaje innecesariamente técnico.
- Explicar el cálculo diferencial también mediante pendientes, áreas y cambios.
- Mantener unidades, signos, dimensiones y supuestos durante todo el desarrollo.
- Conectar los temas con ciencias farmacéuticas cuando sea útil.

El tono puede parecerse al de un profesor que desarrolla con calma una idea en
la pizarra: cercano, razonado y preciso.

## Revisión de cada apunte

Antes de considerar terminado un archivo, comprobar:

- [ ] La portada ocupa una página e incluye `Profesor: Diego García`.
- [ ] El índice ocupa la segunda página.
- [ ] El contenido comienza inmediatamente después del índice.
- [ ] La numeración del contenido comienza en `1`.
- [ ] No aparecen propósito, objetivos, fuentes ni preparación docente.
- [ ] El mapa inicial contiene conceptos físicos unidos por flechas.
- [ ] El artículo puede trasladarse directamente a la pizarra.
- [ ] No existen instrucciones sobre qué debe decir o hacer el docente.
- [ ] Las definiciones están completas y conectadas con una necesidad física.
- [ ] Los símbolos, unidades, signos y supuestos están explicados.
- [ ] Las derivaciones importantes muestran sus pasos.
- [ ] Los dibujos y gráficos aparecen realmente en el documento.
- [ ] Los ejemplos numéricos quedan completamente resueltos.
- [ ] Solo se usan bloques morados para ejemplos cualitativos.
- [ ] Solo se usan bloques azules para preguntas conceptuales.
- [ ] Los bloques de color son escasos, claros y pertinentes.
- [ ] La síntesis final también corresponde a contenido de pizarra.
- [ ] La extensión responde al contenido y no a un límite rígido.
- [ ] Las fuentes utilizadas quedaron registradas en `cobertura.txt`.

## Compilación

Desde la carpeta de la semana:

```bash
make pdf
```

Para limpiar archivos auxiliares:

```bash
make clean
```

Después de compilar, el PDF debe revisarse visualmente. Hay que comprobar que
la portada y el índice ocupen exactamente una página cada uno, que la materia
comience en la página siguiente y que ecuaciones, dibujos y bloques no queden
divididos de forma confusa.
