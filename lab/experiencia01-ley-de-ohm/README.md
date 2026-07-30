# Experiencia 01 - Ley de Ohm: voltaje en una resistencia

> **Prototipo estructural. No publicar.**

Esta carpeta prueba el flujo completo de una experiencia local y su detección
por `scripts_canvas/`. El contenido físico pertenece a la Unidad IV y aparece
en la semana 15 de la distribución oficial. El número 01 identifica únicamente
esta prueba; no redefine el Reporte 01 del syllabus.

## Pregunta experimental

¿La caída de voltaje en una resistencia fija es proporcional a la corriente
que la atraviesa dentro del intervalo seguro del montaje?

## Evidencia esperada

- medición de la resistencia con el circuito desenergizado;
- al menos seis pares de corriente y voltaje;
- gráfico de \(V\) en función de \(I\);
- ajuste lineal cuya pendiente estime la resistencia;
- comparación entre resistencia nominal, medición con ohmímetro y pendiente;
- conclusión que distinga evidencia compatible con la ley de Ohm de una mera
  repetición de la ecuación.

## Estructura

- `guia/`: instructivo para estudiantes y PDF que detecta Canvas.
- `rubrica/`: criterios explícitos y PDF que detecta Canvas.
- `template/`: documento editable del reporte.
- `instrumentos/`: inventario funcional y verificaciones pendientes.
- `datos/`: esquema de registro y análisis.
- `guia-docente.md`: conducción de la sesión y control de riesgos.
- `../slides_exp01/`: presentación Beamer separada, nunca cargada por el script.

## Bloqueos antes de una aplicación real

1. Confirmar marca, modelo, rango, resolución y fusible de cada multímetro.
2. Confirmar rango y límite de corriente de la fuente DC.
3. Confirmar valor nominal, tolerancia y potencia máxima de la resistencia.
4. Calcular y ensayar el intervalo seguro de voltaje y corriente.
5. Registrar datos piloto.
6. Confirmar la numeración oficial de la experiencia y del reporte.
7. Sustituir o eliminar el marcador `NO_PUBLICAR` solo después de esas
   verificaciones.

## Fuentes

- Syllabus oficial: AE 04, ley de Ohm y Reporte 04.
- Distribución oficial: Unidad IV, semana 15.
- `general/1Clases.pdf`: páginas PDF 169-172, resistencia, voltaje, corriente y
  ley de Ohm.
- `general/martins-2011.pdf`: páginas PDF 249-251, resistencia y conductancia
  de soluciones electrolíticas como puente químico-farmacéutico.
