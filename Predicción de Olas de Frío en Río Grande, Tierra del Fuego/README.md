
<div align="center">
    <img src="https://github.com/user-attachments/assets/c4cd115d-c880-4ee1-9ebc-67cfc9b914b9" alt="Portada del Proyecto" width="800">
</div>



# Predicción de Olas de Frío en Río Grande, Tierra del Fuego
## Link del video: https://drive.google.com/file/d/1iUNejZsGjgP-iPX2SjzOjstZKuzfpfV9/view?usp=sharing

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Las olas de frío pueden tener efectos severos en la población y en las infraestructuras. Este proyecto utiliza datos meteorológicos de Río Grande, Tierra del Fuego para entrenar un modelo de clasificación binaria que permite anticipar estos eventos y mejorar la toma de decisiones en climatología.

## Objetivo
El proyecto tuvo como objetivo desarrollar un modelo de Aprendizaje Automático capaz de predecir una ola de frío en la ciudad de Río Grande, Tierra del Fuego, a partir de variables meteorológicas históricas, con el fin de anticipar eventos climáticos y contribuir a la toma de decisiones preventivas. 

## Contexto del Problema
Dada la ubicación geográfica y el clima predominantemente frío de la región, predecir de forma anticipada la ocurrencia de una ola de frío es un desafío con alto valor social y técnico. Si bien existen métodos meteorológicos para el monitoreo, este proyecto explora el potencial del Aprendizaje Automático.  El desarrollo de un modelo predictivo de este tipo requiere abordar distintos aspectos: desde la definición objetiva de lo que se considera una “ola de frío” hasta el tratamiento de datos desbalanceados, pasando por la selección adecuada de variables y modelos. En este sentido, el trabajo busca responder preguntas clave como: 

¿Cómo se puede identificar una ola de frío utilizando datos históricos de temperatura?

¿Qué tipo de modelo de clasificación permite predecir estos eventos con mayor eficacia?

¿Qué grado de precisión puede alcanzarse en la predicción de eventos poco frecuentes?

## Conclusiones

En este proyecto se desarrolló un modelo de clasificación binaria capaz de predecir una ola de frío en Río Grande, Tierra del Fuego, con datos meteorológicos correspondientes al periodo 2021-2024.  En él se entrenaron dos algoritmos, un Árbol de decisión y Random Forest del cual este último fue el que mejores resultados proporcionó. 
Estos resultados permiten concluir que el modelo Random Forest es efectivo para anticipar olas de frío en la región analizada, representando una herramienta útil para la toma de decisiones en contextos de prevención climática.

Como recomendaciones para trabajos futuros sugiero:

- Incluir datos de más años o de otras variables meteorológicas regionales (presión en zonas vecinas, humedad del suelo, etc.)

- Explorar otros algoritmos más avanzados como XGBoost o LightGBM

- Ajustar el umbral de decisión según el tipo de aplicación (conservador o sensible)

- Complementar el modelo con sistemas de alerta temprana o mapas climáticos





## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         prediccion_olas and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── prediccion_olas   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes prediccion_olas a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

