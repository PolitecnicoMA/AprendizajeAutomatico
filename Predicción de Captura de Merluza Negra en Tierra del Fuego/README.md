<p align="center">
  <img src="Merluza_Negra_Portada_Git.png.png" alt="Portada Merluza Negra" width="800"/>
</p>

<h1 align="center">Predicción de Captura de Merluza Negra en Tierra del Fuego</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-blue"/>
  <img src="https://img.shields.io/badge/Python-3.10-blue"/>
  <img src="https://img.shields.io/badge/Licencia-MIT-green"/>
</p>

Este proyecto aplica técnicas de Aprendizaje Automático para predecir la captura mensual de Merluza Negra en la provincia de Tierra del Fuego, Argentina, utilizando variables climáticas y oceanográficas.

---

## Descripción del problema

Se busca modelar y predecir la variable `captura` mensual utilizando los valores de `anom` (anomalía de temperatura superficial del mar, SST). El modelo utilizado corresponde a una regresión supervisada (lineal simple), entrenado sobre datos reales del año 2019.

---

## Técnicas aplicadas

- Preprocesamiento de datos (filtrado, fechas, merge, normalización) con `pandas` y `numpy`
- Visualización de dispersión y densidad con `matplotlib` y `seaborn` (KDE e histogramas)
- Entrenamiento del modelo con `scikit-learn` (regresión lineal y Random Forest)
- Evaluación del modelo (MAE y R²)

---

## Comparación de Modelos

| Modelo             | MAE (kg) | R²    |
|--------------------|----------|-------|
| Regresión Lineal   | 750      | 0.74  |
| Random Forest      | 620      | 0.81  |

---

## Estructura del Proyecto

Organizado según la arquitectura de [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/):


```
├── data/             # Datos
│   ├── raw/          # Datos originales reales (Merluza y SST 2019)
│   ├── interim/      # Datos intermedios
│   └── processed/    # Datos listos para modelar
├── notebooks/        # Jupyter Notebooks
├── src/              # Código fuente del proyecto
├── reports/          # Visualizaciones, gráficos y salidas
├── docs/             # Documentación (PDFs, Word, etc.)
└── README.md         # Este archivo

```

---

## Herramientas utilizadas

- Python, Pandas, NumPy, scikit-learn
- Jupyter Notebook
- Git y GitHub

---

## Importante

Este repositorio no incluye datos sensibles o pesados por decisión consciente. Las carpetas `data/` están estructuradas y listas para recibir los archivos `.csv` reales, que deben mantenerse localmente.

---

## Fuentes de los datos

Este proyecto utiliza datasets públicos y confiables, correspondientes al año 2019, obtenidos de las siguientes fuentes oficiales:

- **Captura mensual de Merluza Negra**  
   [Subsecretaría de Pesca y Acuicultura - Capturas marítimas (datos.gob.ar)](https://datos.gob.ar/dataset/agroindustria-pesca---desembarques-capturas-maritimas)

- **Anomalías de Temperatura Superficial del Mar (SST)**  
  [NOAA - National Centers for Environmental Information](https://www.ncei.noaa.gov/access)

- **Datos Climáticos de Ushuaia y Río Grande**  
  [NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/)

Estas fuentes se usaron exclusivamente con fines académicos para el entrenamiento y análisis del modelo de regresión supervisada.

---
## Presentación del Proyecto

- En la carpeta /videos, se puede descargar la presentacion haciendo click en - "Cristiancouto Prediccion Captura Merluza Negra.mp4" y luego en "view raw".

-  Este video explica el desarrollo completo del proyecto de predicción de captura de merluza negra, desde el análisis de datos hasta los resultados obtenidos con el modelo Random Forest.

---

## Autor

**Cristian Couto**  
Tierra del Fuego, Argentina  
Estudiante de la Tecnicatura en Ciencia de Datos e Inteligencia Artificial  
Centro Politécnico Malvinas Argentinas  
Proyecto académico para la materia Aprendizaje Automático

Contacto: [GitHub](https://github.com/CristianCouto)

---

## Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).
