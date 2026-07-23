# Publicación del material en Canvas

Estos scripts publican los PDF semanales de **DFFR300 — Física Aplicada a las
Ciencias Farmacéuticas** en el módulo `Material del curso`.

## Estructura del módulo

```text
UNIDAD I: MECÁNICA DE LA PARTÍCULA EN UNA DIMENSIÓN
    Semanas 01–06
UNIDAD II: MECÁNICA DE FLUIDOS
    Semanas 07–08
UNIDAD III: TEMPERATURA, CALOR Y TERMODINÁMICA
    Semanas 09–12
UNIDAD IV: ELECTRICIDAD Y MAGNETISMO
    Semanas 13–16
```

Cada semana contiene dos PDF, por ejemplo:

```text
lectures/semana01/semana01-P1.pdf
lectures/semana01/semana01-P2.pdf
```

La estructura completa tiene 52 items: 4 encabezados de unidad, 16 encabezados
semanales y 32 PDF.

## Configuración

Instalar dependencias:

```bash
python -m pip install -r scripts_canvas/requirements.txt
```

`scripts_canvas/Key.txt` usa una línea por profesor:

```text
Profesor|TokenCanvas|CourseID
```

El archivo está excluido de Git. También se pueden configurar rutas externas:

- `CANVAS_KEY_FILE`: archivo de credenciales.
- `CANVAS_LECTURES_DIR`: directorio que contiene `semana01/`, etc.
- `CANVAS_SOLEMNES_DIR`: directorio de evaluaciones.

## Uso seguro

El modo predeterminado es TEST y exige seleccionar usuarios explícitamente:

```bash
python scripts_canvas/subir_semana.py --semana 1 --usuarios Profesor
```

Para probar con todos los usuarios configurados:

```bash
python scripts_canvas/subir_semana.py --semana 1 --todos
```

Producción debe solicitarse expresamente:

```bash
python scripts_canvas/subir_semana.py --semana 1 --usuarios Profesor --produccion
```

Los nombres locales permanecen fijos, pero los títulos visibles se pueden
personalizar independientemente:

```bash
python scripts_canvas/subir_semana.py \
  --semana 1 \
  --usuarios Profesor \
  --titulo-semana "Semana 01 — Introducción al lenguaje de la física" \
  --titulo-p1 "Clase 1 — Magnitudes, unidades y medición" \
  --titulo-p2 "Clase 2 — Vectores y sistemas de referencia"
```

Se puede entregar solo uno de los títulos. Los argumentos omitidos conservan
el valor predeterminado. Si `--titulo-semana` no comienza con el número de la
semana, el script antepone automáticamente `Semana XX |` para poder reconocerla
y reemplazarla correctamente en ejecuciones posteriores.

Antes de conectarse o modificar Canvas, `subir_contenido()` comprueba que existan
los dos PDF locales. El modo TEST usa `Material del curso TEST`, no publica el
módulo y no elimina archivos globales de Canvas Files.

## Inspección desde Python

```python
import sys
sys.path.insert(0, "scripts_canvas")
import Canvas_Key

Canvas_Key.ver_estructura_base()
```
