
# 📄 Descripción del Dataset Original – Catálogo INPRES 2021–2024

## 🗂 Fuente
- **Documento**: Catálogo Sismológico de Referencia de Tierra del Fuego – Complemento 2021-2024
- **Instituciones responsables**:
  - Estación Astronómica Río Grande (FCAG-UNLP)
  - Universidad Nacional de Tierra del Fuego
  - Centro de Investigaciones Geofísicas (UNLP)
- **Acceso**: Público
- **Formato original**: PDF con tablas semiestructuradas
- **Extracción**: Librería `tabula-py` + revisión manual

## 📊 Descripción del contenido

| Atributo                                      | Descripción                                                                 | Tipo de dato
|-----------------------------------------------|-----------------------------------------------------------------------------|-------------------|
| N°                                            | Número de evento registrado                                                 | Entero            |
| Año, Mes, Día, Hora, Minuto, Segundo          | Fecha y hora del evento                                                     | Entero / Decimal  |
| L                                             | Tipo de evento según distancia epicentral (Local, Regional, Distante)       | Categórico        |
| Latitud, Longitud                             | Coordenadas del epicentro                                                   | Float             |
| Profundidad                                   | Profundidad del evento sísmico en km                                        | Float / String    |
| Error en hora, latitud, longitud, profundidad | Márgenes de error asociados a cada medición                                 | Float / String    |
| NST                                           | Número de estaciones que registraron el evento                              | Entero            |
| RMS                                           | Residual cuadrático medio de tirmpos de viaje (s)                           | Float             |
| GAP                                           | Cobertura azimutal residual                                                 | Entero            |
| ML                                            | Magnitud local del evento                                                   | Float             |
| Agencia de cálculo                            | Institución que reportó el evento (ej. EAR)                                 | Categórico        |

## 📈 Cantidad de datos
- Instancia: **240 eventos sísmicos** registrados entre enero de 2021 y noviembre de 2024.
- Atributos: 20

## ⚠️ Observaciones importantes
- Algunos valores de profundidad tienen letra **“F”** indicando que fueron fijados por criterio técnico.
- El dataset fue luego enriquecido con:
  - Cálculo de distancias a ciudades
  - Ciudad más cercana
  - Variable binaria "significativo"
  - Variables temporales separadas

## 📥 Archivo fuente
📄 [`data/catalogo_sismico_INPRES_2021_2024.pdf`](../data/catalogo_sismico_INPRES_2021_2024.pdf)

---

Este documento describe el dataset en su forma **original**, previo a cualquier transformación o limpieza, y respalda la trazabilidad de los datos usados en el proyecto.



