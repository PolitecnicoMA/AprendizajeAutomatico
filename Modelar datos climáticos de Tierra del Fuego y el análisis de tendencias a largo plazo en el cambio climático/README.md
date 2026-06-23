![Texto alternativo](docs/logo.jpg)


Trabajo Final Aprendizaje Automatico
==============================

Profesor:
Martín Mirabete

Alumno:
Quinteros Francisco Nicolas

Objetivo:
El objetivo principal de este proyecto es aplicar técnicas de aprendizaje automático para
analizar y modelar datos climáticos de Tierra del Fuego, centrándome en la predicción de
temperatura y precipitaciones, la clasificación de eventos climáticos extremos, la detección de
anomalías, y el análisis de tendencias a largo plazo en el cambio climático.
Descripción del Problema:
Abordaré cuatro problemas clave en este proyecto:
1. Predicción de Temperatura o Precipitaciones: Pronosticar la temperatura y las
precipitaciones en el futuro cercano utilizando modelos de series temporales. Las
predicciones precisas son fundamentales para la planificación y mitigación de los
efectos de eventos climáticos extremos, lo cual es importante para las comunidades
locales y sectores como la agricultura.
2. Clasificación de Eventos Climáticos Extremos: Identificar si un día está propenso a
experimentar eventos climáticos extremos, como tormentas u olas de calor,
basándome en variables como la temperatura, la humedad y la presión. Esta
clasificación puede ayudar a anticipar condiciones peligrosas.
3. Detección de Anomalías en Datos Climáticos: Detectar patrones inusuales en los datos
climáticos, como temperaturas extremadamente altas o bajas, o precipitaciones
inesperadas. La identificación de estas anomalías puede señalar cambios drásticos en
el clima y servir como una alerta temprana.
4. Análisis de Tendencias y Cambio Climático: Analizar si ha habido un cambio a lo largo
de los años en variables como la temperatura o las precipitaciones, para identificar
posibles señales de cambio climático. Este análisis ayudará a comprender cómo el
clima está cambiando a largo plazo y su impacto en la región.

Preguntas de Investigación o Hipótesis:

• ¿Es posible predecir con precisión la temperatura y las precipitaciones en mi ciudad
utilizando modelos de series temporales?

• ¿Se pueden clasificar con éxito los días con riesgo de eventos climáticos extremos en
función de las condiciones meteorológicas?

• ¿Qué anomalías climáticas podemos detectar en los datos históricos? ¿Están
relacionadas con fenómenos climáticos globales?

• ¿Existen tendencias claras que sugieran un cambio climático en la región?

Este proyecto busca obtener respuestas a estas preguntas utilizando un enfoque basado en
datos, aplicando algoritmos de aprendizaje automático.


RELEVANCIA


    planificar actividades agrícolas, especialmente en zonas donde la nieve puede impactar el riego, la fertilidad del suelo o los cultivos sensibles al frío.


    Servicios públicos y seguridad: preparas la infraestructura y los recursos 
    ante las inclemencias climáticas

    Tener información respecto del aumento relativo de la temperatura para implementar medidas de sostenibilidad, como la transición a energías renovables

    Economia: turismo en una region en la que el clima es parte fundamental
    en actividades de invierno


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
