# Proyecto de Aprendizaje Automático
## Segmentación de Siniestros Viales mediante K-Means

**Alumna:** Rojas, Paola

---

## 1. Descripción del Proyecto

El proyecto consiste en aplicar técnicas de Aprendizaje Automático No Supervisado para identificar patrones y agrupamientos de siniestros viales ocurridos en las autopistas urbanas durante el año 2024.

A partir de variables relacionadas con la ubicación del accidente, las condiciones meteorológicas, el estado de la vía, el horario y los vehículos involucrados, se buscará detectar grupos de siniestros con características similares.

La finalidad es comprender mejor el comportamiento de los accidentes y descubrir patrones ocultos que permitan identificar zonas, horarios o condiciones asociadas a una mayor concentración de eventos viales.

---

## 2. Formulación de Objetivos

### Objetivo General

Aplicar técnicas de agrupamiento (clustering) para identificar segmentos o patrones de siniestros viales con características similares, utilizando información geográfica, temporal y contextual del dataset.

### Objetivos Específicos

- Analizar y comprender la estructura del dataset de siniestros viales.
- Preparar y transformar los datos para su utilización en algoritmos de clustering.
- Identificar grupos de siniestros similares considerando variables como autopista, punto kilométrico, horario, condiciones meteorológicas y tipo de siniestro.
- Aplicar el algoritmo K-Means para segmentar los registros en diferentes clusters.
- Comparar distintos valores de k mediante el Método del Codo y el Silhouette Score para determinar la cantidad adecuada de grupos.
- Interpretar las características principales de cada cluster encontrado y describir los patrones identificados.

---

## 3. Contexto del Problema y Relevancia

### Contexto

Los siniestros viales representan uno de los principales problemas de seguridad en las grandes ciudades. La ocurrencia de accidentes está influenciada por múltiples factores, entre ellos las condiciones climáticas, el estado de la vía, el horario, el tipo de vehículo involucrado y la ubicación geográfica donde ocurre el hecho.

Las autopistas urbanas presentan características diferentes según el tramo, el sentido de circulación y el flujo vehicular, lo que genera distintos escenarios de riesgo.

### Relevancia

Identificar patrones de siniestralidad permite comprender mejor cómo se comportan los accidentes en diferentes contextos.

Los resultados obtenidos podrían ser utilizados para:

- Identificar horarios con mayor concentración de accidentes.
- Analizar la influencia de las condiciones climáticas.
- La planificación de medidas preventivas y de seguridad vial.
- Optimizar la distribución de recursos de asistencia y emergencia.

---

## 4. Definición del Tipo de Problema

El presente proyecto corresponde a un problema de **Aprendizaje No Supervisado**.

No existe una variable objetivo o etiqueta que indique previamente a qué grupo pertenece cada siniestro.

El propósito del análisis es descubrir patrones ocultos y agrupamientos naturales dentro de los datos mediante técnicas de clustering.

El algoritmo buscará formar grupos de siniestros que compartan características similares, permitiendo identificar distintos perfiles de accidentes sin necesidad de contar con categorías predefinidas.

---

## 5. Modelo de Aprendizaje Automático Propuesto

### K-Means

El algoritmo K-Means es una técnica de clustering ampliamente utilizada en problemas de segmentación de datos.

Su funcionamiento consiste en agrupar observaciones similares en diferentes clusters a partir de la distancia entre los registros y los centroides de cada grupo.

En este proyecto, K-Means permitirá:

- Identificar patrones de siniestros con características similares.
- Descubrir perfiles de accidentes sin contar con categorías previamente definidas.
- Analizar la relación entre variables como tipo de vehículo, cantidad de lesionados, horario y condiciones del siniestro.
- Segmentar los registros en grupos que facilitan la interpretación y comprensión de la siniestralidad vial.

La cantidad óptima de clusters será determinada mediante:

- Método del Codo
- Silhouette Score

Estos métodos permitirán justificar la selección del valor de k más adecuado para representar la estructura de los datos.

### Dataset Utilizado

El proyecto utilizará el dataset **siniestros-2024.csv**, que contiene información sobre accidentes ocurridos en autopistas urbanas durante el año 2024.

Las principales variables analizadas serán: Fecha, Hora, Autopista, Banda y/o Ramal, Pk, Condiciones Meteorológicas, Superficie De La Vía, Lesionados, Fallecidos, Tipo De Siniestro, Moto, Liviano, Bus, Camión.

### Links de presentaciones

Presentación del proyecto en video: https://drive.google.com/file/d/1_HTM_VT8xUj7lUrfqxRtzx4xtAoFNnNO/view?usp=sharing

Link Jupyter Notebook (código): https://colab.research.google.com/drive/1GqXUXI_N7HKy0D94UuaQJ5Kt3XC-btHx?usp=sharing

Presentación del proyecto en PowerPoint: https://docs.google.com/presentation/d/18ChYaIVB6e53XMO9DWVB7Qum2m6foEOc/edit?usp=sharing&ouid=117406770979963466684&rtpof=true&sd=true