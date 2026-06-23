![](https://github.com/ziodoxe/acceso_a_internet/blob/main/reports/figures/banner_politecnico_malvinas.jpg)


###################################################################################################
# LINK DEL VIDEO: https://drive.google.com/file/d/1VSvW3x6EcnB_ylO0r09NSeueu27NmY9C/view?usp=sharing
###################################################################################################

# Análisis de Acceso a Internet en la Provincia de Tierra del Fuego e IAS

## Objetivo
-------------

Este proyecto se centra en el análisis y predicción al acceso a internet utilizando diversas técnicas de ciencia de datos y aprendizaje automático. El objetivo es identificar patrones en los datos sobre el uso de otras tecnologías de la información y comunicación y desarrollar modelos predictivos para clasificar al individuo su cercania con la tecnologia, etiquetandolo como MEDIO, BAJO, ALTO.


## Contexto
-------------

Nos ubicamos en Argentina más precisamente en la Provincia de Tierra del Fuego, donde la acceso a internet es limitado con respecto a las demás provincias del país, esto debido a la localización geografica en la que nos encontramos. A esto se suma que no hay demasiada inversión ni demasiada competencia de parte del sector privado. De parte del estado se provee ayuda en centros tecnológicos, ofreciendo el acceso a internet gratuito.
Mediante una encuesta realizada por el INDEC en 2018 a nivel nacional, se tratará de responder a las siguientes preguntas haciendo foco en la Provincia de Tierra del Fuego y sus localidades de Rio Grande y Ushuaia.

Preguntas a responder:
1) ¿Qué factores determinan si un hogar tiene acceso a internet?
2) ¿Cuáles son las principales características que distinguen a los hogares que usan internet de aquellos que no lo usan?
3) ¿Cómo se pueden agrupar los hogares según su uso de tecnologías de la información y la comunicación?


Los detalles de la descripción del dataset se encuentran en el archivo [DescripcionDeDatos.md](https://github.com/ziodoxe/acceso_a_internet/blob/main/docs/DescripcionDeDatos.md) que se encuentra en la carpeta 'docs'.

El siguiente link provee el origen del dataset a estudiar.
`<link>` : <https://sitioanterior.indec.gob.ar/bases-de-datos.asp> más precisamente en la pestaña de Ciencia y Tecnologia.

**Licencia: MIT**

## Estructura del Proyecto
-------------

La estructura del proyecto esta basada en la plantilla Cookiecutter Data Science:



    ├── LICENSE
    ├── Makefile           <- Makefile comandos como `make data` o `make train`.
    ├── README.md          <- El archivo raiz README para desarrolladores que utilizan este proyecto.
    ├── data
    │   ├── external       <- Data para fuentes de terceros.
    │   ├── interim        <- Datos intermedios que han sido transformados.
    │   ├── processed      <- TLos conjuntos de datos canónicos finales para el modelado.
    │   └── raw            <- El volcado de datos original e inmutable.
    │
    ├── docs               <- Un proyecto Sphinx predeterminado; ver sphinx-doc.org para más detalles.
    │
    ├── models             <- Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos.
    │
    ├── notebooks          <- Jupyter notebooks. La convención de nomenclatura es un número (para realizar 
    │                       pedidos), las iniciales del creador y una breve descripción delimitada por `-`, 
    │                       por ejemplo.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Diccionarios de datos, manuales y todos los demás materiales explicativos.
    │
    ├── reports            <- Análisis generados como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos y figuras generados que se utilizarán en los informes.
    │
    ├── requirements.txt   <- El archivo de requisitos para reproducir el entorno de análisis, por ejemplo.
    │                         generados con `pip freeze > requirements.txt`
    │
    ├── setup.py           <- hace que el proyecto pip sea instalable (pip install -e .) para que se pueda 
    │                      importar src
    ├── src                <- Código fuente para usar en este proyecto.
    │   ├── __init__.py    <- Hace que src sea un módulo de Python
    │   │
    │   ├── data           <- Scripts para descargar o generar datos.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para convertir datos sin procesar en funciones para modelar
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para entrenar modelos y luego usar modelos entrenados para 
    │   │   │              hacer predicciones
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear visualizaciones exploratorias y orientadas a resultados.
    │       └── visualize.py
    │
    └── tox.ini            <- archivo tox con configuraciones para ejecutar tox; ver tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


```sh
ENGLISH VERSION
```
# Analysis of Internet Access in the Province of Tierra del Fuego and IAS

## Objetive
-------------
This project focuses on the analysis and prediction of internet access using various data science and machine learning techniques. The objective is to identify patterns in the data on the use of other information and communication technologies and develop predictive models to classify the individual's proximity to the technology, labeling it as MEDIUM, LOW, HIGH.

## Context
-------------
We are located in Argentina, more precisely in the Province of Tierra del Fuego, where internet access is limited compared to the other provinces of the country, due to the geographical location in which we are located. Added to this is that there is not much investment or much competition from the private sector. On behalf of the state, help is provided in technology centers, offering free internet access.
Through a survey carried out by INDEC in 2018 at the national level, an attempt will be made to answer the following questions, focusing on the Province of Tierra del Fuego and its towns of Rio Grande and Ushuaia.

Questions to answer:
What factors determine whether a person has access to the internet?
What are the main characteristics that distinguish people who use the Internet from those who do not use it?
How can people be grouped according to their use of information and communication technologies?

The details of the dataset description are found in the file [DescripcionDeDatos.md](https://github.com/ziodoxe/acceso_a_internet/blob/main/docs/DescripcionDeDatos.md) located in the 'docs' folder.

The following link provides the origin of the dataset to be studied. `<link>` : <https://sitioanterior.indec.gob.ar/bases-de-datos.asp> more precisely in the Science and Technology tab.

**License: MIT**

### Project Organization
-------------


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
