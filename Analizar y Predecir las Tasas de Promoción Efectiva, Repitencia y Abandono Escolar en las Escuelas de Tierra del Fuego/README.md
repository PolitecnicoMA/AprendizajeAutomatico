![](https://github.com/lucasgab2010/tpfinal_AA/blob/main/docs/logo.jpg)

![](https://github.com/lucasgab2010/tpfinal_AA/blob/main/docs/escuela.jpg)


# Trabajo Práctico de Aprendizaje Automático

## Analizar y Predecir las Tasas de Promoción Efectiva, Repitencia y Abandono Escolar en las Escuelas de Tierra del Fuego
### Profesor
**Martín Mirabete**
### Alumno
**Gabriel García**

## Video
[![Vista Previa del Video](https://github.com/lucasgab2010/tpfinal_AA/blob/main/docs/clases.jpg)](https://drive.google.com/file/d/1A63zm3anZTns6dX2gjZ92P5uLL6XCajW/view?usp=sharing)

## Presentación

[Haz clic aquí para ver la presentación](https://docs.google.com/presentation/d/1yQOuUfuDL5Rtm-d7KUYTR_PzFKC2QpyJSiHnglHW4_0/pub?start=false&loop=false&delayms=3000)

---
## Prediction and Improvement of Educational Results in Schools in Tierra del Fuego

## Abstract:

This study aims to analyze and predict promotion rates, repetition, and school 
dropout in Tierra del Fuego schools. It identifies factors influencing these
indicators to improve policies. Data on socioeconomic factors, school
characteristics, and contextual elements are collected, cleaned, normalized, and
used to build predictive models. Specifically, a linear regression model is
employed to forecast non-promotion rates in secondary schools. Models are
validated with high accuracy using separate test sets. Evaluation metrics like
MSE, RMSE, MAE, and R2 gauge model performance. Recommendations
include personalized tutoring, enhanced teacher training, and community
engagement to support at-risk students. Additional resources for lower
socioeconomic schools are advised. These interventions aim to boost promotion
rates, lower repetition, and dropout rates, optimizing educational outcomes in
Tierra del Fuego for a more equitable and effective system.

## Descripción y Formulación del Objetivo

### Definición del Problema

El objetivo del proyecto es analizar y predecir las tasas de promoción efectiva, repitencia y abandono escolar en las escuelas de Tierra del Fuego. Se busca identificar los factores que influyen en estos indicadores educativos y utilizar esta información para mejorar las políticas y prácticas educativas.

---

## Recolección y Preparación de Datos

### Variables Relevantes

- **Dependientes:**
  - Tasa de promoción efectiva
  - Tasa de repitencia
  - Tasa de abandono interanual

- **Independientes:**
  - Datos socioeconómicos de los estudiantes (ingresos familiares, nivel educativo de los padres, etc.)
  - Características de las escuelas (ubicación, recursos, infraestructura, número de estudiantes, ratios alumno/profesor)
  - Factores contextuales (desempleo en la región, acceso a servicios básicos, etc.)

### Acciones

- Cargar los datos y revisar su estructura.
- Limpiar los datos, manejando valores faltantes y eliminando registros inconsistentes.
- Codificar variables categóricas si es necesario.

---

## Objetivo del Trabajo

El objetivo de este proyecto es analizar y predecir las tasas de promoción efectiva, repitencia y abandono escolar en las escuelas de Tierra del Fuego. Este análisis se enfocará en identificar los factores socioeconómicos, institucionales y contextuales que influyen significativamente en estos indicadores educativos.

### Problema Específico

El problema específico que se abordará con este modelo es la identificación y comprensión de los factores que afectan negativamente la continuidad educativa de los estudiantes en Tierra del Fuego. Al predecir las tasas de promoción, repitencia y abandono, se pretende:

- **Identificar Variables Clave:** Determinar cuáles son los factores más influyentes en las tasas de promoción, repitencia y abandono escolar.
- **Predecir Indicadores Educativos:** Desarrollar modelos predictivos que permitan anticipar las tasas de promoción, repitencia y abandono en diferentes escuelas y regiones.
- **Proporcionar Recomendaciones:** Ofrecer recomendaciones específicas para mejorar las políticas educativas y las prácticas escolares.
- **Mejorar la Eficiencia de Recursos:** Ayudar a las autoridades educativas a asignar recursos de manera más eficiente y dirigida.

---

## Contexto del Problema

### Situación Educativa en Tierra del Fuego

En Tierra del Fuego, como en otras provincias de la Argentina, se enfrenta a desafíos significativos en su sistema educativo. Aunque ha habido avances en el acceso a la educación, persisten problemas relacionados con la calidad de la educación y la equidad en el acceso y los resultados educativos. Algunos de los principales indicadores que reflejan estos desafíos son las tasas de promoción efectiva, repitencia y abandono escolar.

- **Tasa de Promoción Efectiva:** Mide el porcentaje de estudiantes que avanzan al siguiente nivel educativo sin repetir el grado. Una tasa alta de promoción efectiva indica un sistema educativo que apoya y retiene a sus estudiantes de manera efectiva.
- **Tasa de Repitencia:** Refleja el porcentaje de estudiantes que deben repetir el grado. Altas tasas de repitencia pueden ser indicativas de problemas en la calidad de la enseñanza, la relevancia del currículo, o de problemas socioeconómicos que afectan el rendimiento estudiantil.
- **Tasa de Abandono Escolar:** Representa el porcentaje de estudiantes que dejan la escuela antes de completar su educación. El abandono escolar es un problema crítico, ya que está asociado con peores resultados en términos de empleo, ingresos y bienestar social a largo plazo.

---

## Relevancia del Problema

La educación es un pilar fundamental para el desarrollo económico y social de cualquier país. En el caso de Tierra del Fuego, mejorar las tasas de promoción efectiva, y reducir las tasas de repitencia y abandono escolar, es crucial por varias razones:

- **Desarrollo Económico:** Una población bien educada es más productiva y tiene mayores oportunidades de empleo. La educación mejora las habilidades y competencias, lo que a su vez impulsa la innovación y el crecimiento económico.
- **Equidad Social:** Las disparidades en los resultados educativos a menudo reflejan y perpetúan desigualdades sociales y económicas. Mejorar los resultados educativos puede ayudar a reducir estas brechas y promover una mayor equidad social.
- **Calidad de Vida:** La educación está estrechamente vinculada a una mejor calidad de vida. Las personas con niveles educativos más altos tienden a tener mejores resultados en términos de salud, participación cívica y bienestar general.
- **Política Pública:** Para los responsables de la formulación de políticas, tener una comprensión clara de los factores que influyen en la promoción, repitencia y abandono escolar es esencial para diseñar intervenciones efectivas.

---

## Relevancia del Proyecto

El análisis y la predicción de las tasas de promoción efectiva, repitencia y abandono escolar en Tierra del Fuego no solo contribuirán a la comprensión de estos fenómenos, sino que también proporcionarán una base sólida para la toma de decisiones informadas. Al identificar los factores que afectan negativamente la continuidad educativa, se pueden diseñar políticas y programas que apoyen mejor a los estudiantes y mejoren los resultados educativos a nivel provincial.

---

## Preguntas de Investigación

Para abordar el problema de las tasas de promoción efectiva, repitencia y abandono escolar en Tierra del Fuego mediante técnicas de aprendizaje automático, formularemos las siguientes preguntas de investigación:

1. ¿Cuáles son los principales factores socioeconómicos, demográficos y académicos que afectan la tasa de promoción efectiva en las escuelas de Tierra del Fuego?
2. ¿Qué variables están más correlacionadas con las tasas de repitencia y abandono escolar?
3. ¿Es posible predecir con precisión la tasa de promoción efectiva de un grupo de estudiantes en función de las características disponibles?
4. ¿Qué tan preciso es el modelo de aprendizaje automático para predecir las tasas de repitencia y abandono escolar?
5. ¿Qué tipo de intervenciones (por ejemplo, tutorías adicionales, programas de apoyo económico) podrían tener el mayor impacto en la reducción de las tasas de repitencia y abandono?

---

## Selección del Modelo

Utilizaremos un modelo de regresión de Aprendizaje Supervisado, probando con un modelo de regresión lineal (`LinearRegression`) para predecir valores continuos. También desarrollaremos un modelo de Árbol de Decisión (`RandomForestRegressor`) para mejorar la precisión y la robustez de las predicciones.

---

## Pasos a Seguir

### Carga de Librerías Necesarias

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
```

## Exploración de Datos
- Análisis general del dataset.
- Análisis descriptivo y estadístico.
- Detección de valores nulos y duplicados.

## Preprocesamiento
- Conversión de fechas a un formato adecuado.
- Codificación de variables categóricas.
- Normalización o estandarización de precios.

## Modelado
- Definición del problema.
- Selección de algoritmos apropiados.
- Entrenamiento y validación del modelo.

## Evaluación
- Métricas de desempeño como MSE y R².
- Interpretación de resultados y conclusiones.

## Conclusión
Este proyecto tiene el potencial de impactar significativamente la política educativa en Tierra del Fuego, proporcionando una comprensión profunda de los factores que afectan la continuidad educativa y permitiendo la creación de estrategias más efectivas para mejorar las tasas de promoción, repitencia y abandono escolar.

---

### Licencia
### Este proyecto está licenciado bajo MIT License.

==============================


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

