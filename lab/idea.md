# Laboratorio del curso

Esta carpeta reúne el material de laboratorio para **Física Aplicada a las Ciencias Farmacéuticas**. El objetivo no es solo acumular instrucciones de experimentos, sino construir una guía coherente que conecte la teoría del curso con mediciones reales, uso de instrumentos, análisis de datos y discusión física.

El laboratorio debe ayudar a estudiantes de primer año a pasar de una idea física abstracta a una pregunta experimental concreta:

- ¿Qué queremos medir?
- ¿Qué fenómeno físico está detrás?
- ¿Qué instrumentos permiten observarlo?
- ¿Qué cuidados requiere la medición?
- ¿Cómo se interpretan los datos obtenidos?

## Propósito pedagógico

Cada experiencia debe estar diseñada para que el estudiante entienda la física básica involucrada y, al mismo tiempo, aprenda una forma razonable de trabajar en laboratorio. La prioridad es que la actividad sea clara, ejecutable y conectada con los contenidos centrales del curso: cinemática, leyes de Newton, fluidos, termodinámica y electromagnetismo.

El laboratorio debe evitar instrucciones mecánicas del tipo "siga estos pasos" sin contexto. Antes de medir, el estudiante debe saber qué pregunta responde el experimento y por qué esa pregunta importa dentro del curso.

## Organización recomendada

Conviene organizar esta carpeta por **experimentos**, no por semanas. Un mismo experimento puede ocupar una o más sesiones, y su ubicación no debería depender rígidamente del calendario.

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

Uso esperado de cada archivo o carpeta:

- `README.md`: descripción general del experimento, objetivo, pregunta experimental y relación con el curso.
- `slides/`: presentación breve para introducir la experiencia antes del trabajo práctico.
- `instrumentos/`: fichas de uso de equipos, imágenes, manuales resumidos y precauciones.
- `datos/`: plantillas de registro, datos de ejemplo o archivos para análisis posterior.
- `guia-estudiante.md`: instrucciones que recibe el estudiante durante la actividad.
- `guia-docente.md`: notas para quien guía la sesión, tiempos sugeridos, errores frecuentes y criterios de intervención.
- `rubrica.md`: criterios de evaluación del informe, bitácora o producto solicitado.

Esta estructura se puede simplificar cuando el experimento sea pequeño, pero la separación entre **fenómeno**, **instrumentación**, **datos** y **evaluación** debería mantenerse.

## Material mínimo por experimento

Cada experiencia debería producir, al menos, dos tipos de material:

1. Una presentación breve para abrir la sesión.
2. Una guía de trabajo para estudiantes.

La presentación no debe reemplazar la actividad. Debe preparar a los estudiantes para medir con sentido y luego dejar tiempo suficiente para el trabajo experimental.

La guía de trabajo debe ser más operativa: debe indicar qué se mide, cómo se registra, qué tabla o gráfico se construye, qué magnitudes se calculan y qué preguntas se responden al final.

## Estructura sugerida de la presentación

La presentación debe ser breve y visual. Una estructura útil es:

1. **Nombre del experimento**
2. **Pregunta experimental**
3. **Fenómeno físico involucrado**
4. **Montaje o idea del experimento**
5. **Instrumentos que se usarán**
6. **Precauciones y errores frecuentes**
7. **Qué datos se deben registrar**
8. **Qué se espera concluir**
9. **Inicio del trabajo práctico**

La introducción debe responder preguntas simples: quién formuló o estudió históricamente el fenómeno, qué problema físico intentaba resolver y qué relación tiene con el curso. No se necesita una historia larga, pero sí una motivación que haga que el experimento tenga sentido.

## Instrumentación

Cada instrumento relevante debe tener una ficha breve. La ficha debe explicar:

- Para qué sirve el instrumento.
- Qué magnitud mide o controla.
- En qué unidades entrega la información.
- Cómo se calibra o verifica antes de usarlo.
- Qué errores de uso son comunes.
- Qué precauciones de seguridad o cuidado requiere.
- Qué rol cumple dentro del experimento.

Cuando no exista un manual interno, se puede construir una ficha adaptando información de manuales del fabricante, material docente o imágenes de referencia. Las imágenes deben ser claras y deben mostrar el instrumento real o uno equivalente.

## Guía para estudiantes

La guía del estudiante debe estar escrita en lenguaje directo y comprensible. Debe evitar párrafos largos y separar claramente instrucciones, preguntas y espacios de registro.

Estructura sugerida:

1. **Objetivo**
2. **Pregunta experimental**
3. **Fundamento físico mínimo**
4. **Materiales e instrumentos**
5. **Montaje**
6. **Procedimiento**
7. **Registro de datos**
8. **Análisis**
9. **Preguntas de cierre**
10. **Producto a entregar**

El fundamento físico no debe repetir toda la clase teórica. Debe recordar las ideas necesarias para interpretar el experimento: ecuaciones relevantes, unidades, supuestos y significado de las variables.

## Guía docente

La guía docente debe permitir que otra persona pueda conducir la sesión sin reconstruir todo desde cero. Debe incluir:

- Duración estimada de cada etapa.
- Qué explicar al inicio y qué dejar para discusión posterior.
- Qué errores conceptuales o experimentales son esperables.
- Qué datos razonables deberían obtenerse.
- Qué hacer si el montaje falla o si el tiempo no alcanza.
- Qué criterios usar para evaluar la actividad.

Esta guía puede ser más técnica que la guía del estudiante, pero debe seguir siendo breve y útil.

## Relación con el curso

Los experimentos deben dialogar con las unidades del curso:

- **Cinemática y dinámica:** medición de posición, velocidad, aceleración, fuerza, fricción o movimiento con resistencia.
- **Fluidos:** densidad, presión, empuje, viscosidad, flujo, continuidad, Poiseuille o tensión superficial.
- **Termodinámica:** temperatura, calorimetría, calor específico, cambios de fase, transferencia de calor o gas ideal.
- **Electricidad y magnetismo:** carga, corriente, resistencia, ley de Ohm, circuitos simples, sensores, campos o inducción.

No todos los experimentos tienen que cubrir una unidad completa. Es mejor que cada experiencia tenga una pregunta clara y bien cerrada a que intente abarcar demasiados contenidos.

## Criterios de diseño

Un buen experimento para este curso debería cumplir con lo siguiente:

- Puede realizarse con el tiempo y equipamiento disponible.
- Tiene una pregunta experimental explícita.
- Produce datos medibles, no solo observaciones cualitativas.
- Obliga a usar unidades, estimar incertidumbre o discutir errores.
- Conecta con una ecuación o principio físico del curso.
- Permite una conclusión breve basada en evidencia.
- Puede evaluarse con criterios claros.

Si una actividad no produce datos suficientes, puede funcionar como demostración, pero entonces debe identificarse como tal y no como experimento completo.

## Flujo de construcción

Para desarrollar un nuevo experimento conviene seguir este orden:

1. Definir la pregunta experimental.
2. Identificar el contenido del curso que se quiere reforzar.
3. Revisar qué instrumentos están disponibles.
4. Diseñar el montaje y el procedimiento.
5. Probar qué datos se obtienen y si son razonables.
6. Escribir la guía del estudiante.
7. Preparar las fichas de instrumentos.
8. Construir la presentación breve.
9. Crear la guía docente y la rúbrica.
10. Ajustar el material después de una primera aplicación.

La presentación se construye al final, no al principio. Primero debe estar claro qué hará el estudiante y qué datos se esperan.

## Cronología

Aún debe definirse si cada experimento ocupará una sesión o más de una. Mientras eso no esté cerrado, conviene diseñar cada experiencia con dos versiones:

- **Versión corta:** introducción breve, medición principal y una conclusión guiada.
- **Versión extendida:** incluye repetición de mediciones, análisis de incertidumbre, gráficos, discusión de errores y preguntas adicionales.

Esto permite adaptar el laboratorio a semanas con feriados, evaluaciones u otros ajustes del calendario.

## Producto esperado del laboratorio

El resultado final de esta carpeta debería ser una colección de experiencias listas para usar. Cada una debe permitir que el docente abra la sesión con una explicación breve, que los estudiantes trabajen con instrumentos reales y que el cierre conecte los datos con una idea física del curso.

La meta no es tener material extenso, sino material claro, verificable y útil en sala.
