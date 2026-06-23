# 🔥 Clasificación de Riesgo de Incendios Forestales en Tierra del Fuego

Este proyecto aplica técnicas de *Machine Learning* para clasificar el **nivel de riesgo de incendio forestal** en la Isla de Tierra del Fuego, Argentina. Se utilizó el índice canadiense **FWI (Fire Weather Index)** para etiquetar los niveles de riesgo a partir de datos meteorológicos obtenidos de la plataforma [Open-Meteo](https://open-meteo.com/).

🎬 Video explicativo del modelo: https://drive.google.com/file/d/1xMGkrJtvcaeIARh-k4RMIBCMK_7nN6A0/view?usp=sharing


## 📊 Objetivo del Proyecto

Desarrollar un modelo de clasificación supervisada que prediga el **nivel de riesgo de incendio forestal** según variables meteorológicas, con el fin de aportar una herramienta predictiva útil para la gestión ambiental y la prevención de incendios.

## 🛰️ Fuente de Datos

Los datos meteorológicos fueron descargados desde la API de **Open-Meteo**, e incluyen las siguientes variables:

- 🌡️ Temperatura (°C)
- 💧 Humedad relativa (%)
- 🌬️ Velocidad del viento (km/h)
- 🌧️ Precipitación (mm)
- 🌱 Humedad volumétrica del suelo (mm³/mm³)

## 🏷️ Etiquetado del Riesgo

La variable objetivo para el riesgo de incendio (`Riesgo`) fue generada aplicando el índice **FWI** del sistema canadiense (https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi), clasificando el riesgo en cinco niveles:

- Bajo
- Moderado
- Alto
- Muy Alto
- Extremo

## 🧠 Modelo Utilizado

Se utilizó el algoritmo **K-Nearest Neighbors (KNN)** para entrenar el modelo de clasificación. El flujo de trabajo incluyó:

1. Carga y exploración de datos.
2. Preprocesamiento: limpieza, normalización y etiquetado.
3. División del dataset en entrenamiento y prueba.
4. Entrenamiento del modelo con KNN.
5. Evaluación del modelo mediante matriz de confusión y métricas de desempeño.

## ⚙️ Tecnologías y Librerías

- Python 🐍
- Scikit-learn
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook
- Google Colab
- API de Open-Meteo

## 📈 Resultados

El modelo logró una precisión adecuada al clasificar correctamente la mayoría de los niveles de riesgo con un *accuracy* de 96%. La matriz de confusión y las métricas como *precision*, *recall* y *f1-score* fueron utilizadas para evaluar el desempeño del modelo y lograron valores por encima del 90%.

## 📌 Consideraciones
Los datos están limitados geográficamente a la región de Tierra del Fuego.

El modelo puede ser mejorado incluyendo más datos, ajustando hiperparámetros o probando otros algoritmos.

La clasificación del riesgo de incendio es compleja y puede requerir consideraciones adicionales

## 📂 Estructura del Repositorio

```bash
📁 forest-fire-risk-tdf/
├── data/                  # Datos meteorológicos crudos o procesados
├── docs/                  # Documentacion del proyecto
├── notebooks/             # Jupyter notebooks con el análisis y entrenamiento
├── models/                # Archivos del modelo entrenado (opcional)
├── references             # referencias
└── README.md              # Este archivo
```
## 📚 Referencias
- [1] https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi
- [2] https://ostrnrcan-dostrncan.canada.ca/entities/publication/29706108-2891-4e5d-a59a-a77c96bc507c
- [3] https://obs-idecor-mapas-docs.obs.sa-argentina-1.myhuaweicloud.com/m442/Indice_FWI_y_componentes.pdf
- [4] https://www.smn.gob.ar/sites/default/files/mapasdepeligro.pdf
- [5] https://www.calculatorultra.com/en/tool/fire-weather-index-calculator.html#gsc.tab=0

## ©️ Licencia y uso

Este trabajo tiene fines academicos el cual permite afianzar conocimientos y tecnicas en ciencia de datos y aprendizaje automatico para el modelado y desarrollo del proyecto.

## 🙋 Autor
**Maximiliano Valentin Ruiz**

📧 Contacto: [maxi9304@gmail.com]

🎓 Estudiante de la Tecnicatura en Ciencia de Datos e Inteligencia Artificial