### *Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial.*
### *Politécnico Malvinas Argentinas.*

## Aprendizaje Automático
Autora: Buccino Anabella.
# **Modificación de factores de riesgo para la prevención de ENT**

##### Entrega 1: Descripción y Formulación del Objetivo

------------

# Objetivo del proyecto
El objetivo del proyecto es estudiar los comportamientos y condiciones de vida de la población de Tierra del Fuego y como afecta la salud de la población de 18 años y más, si modificando algunos de los hábitos las personas pueden retardar, mejorar o prevenir ciertos factores de riesgo que predisponen la aparición de enfermedades no transmisibles (ENT)

# Contexto y Relevancia del problema
Tierra del Fuego es la provincia mas austral de Argentina que de acuerdo a sus condiciones tanto demográficas como socioeconómicas influyen en la salud de la población. Su ubicación remota, el acceso a la salud y el clima extremo generan desafíos particulares en el estilo de vida de la población.
Las enfermedades no transmisibles como la diabetes, la hipertensión arterial, los accidentes cardiovasculares, obesidad, entre otras son causantes de mortalidad y discapacidad en todo el mundo, incluyendo a Tierra del Fuego. Los factores de riesgo como sedentarismo, tabaquismo, alcoholismo, como muchos otros factores están estrechamente relacionados con estas enfermedades. 
Por tal motivo la prevención y cuidados son fundamentales, estudiar los comportamientos y condiciones de vida de la población de Tierra del Fuego y su relación con la salud de los adultos es un problema relevante con el potencial de generar un impacto significativo en la salud pública, la equidad y el bienestar de la población. El proyecto tiene un enfoque integrador para mejorar la salud poblacional.


# Preguntas de hipótesis o preguntas de investigación:
El Proyecto debe responde a la pregunta de ¿si se modifica alguno de los factores de riesgo bajarían las tasas de ENT?
Para que se pueda llevar a cabo debe existir una correcta utilización de los datos y cuales son los factores a modificar.


------------

##### Entrega 2: Descripción del Dataset y Origen

-	Obtención de los datos: los datos son provenientes de la página del inced de la Encuensta Nacional de Factores de Riesgo del 2018.
-	Integración y limpieza de los datos provenientes de las distintas fuentes.
-	Análisis exploratorio de los datos en busca de comprender mejor los datos y de acuerdo a la limpieza de los datos se va a tener en cuenta las variables que puedan proporcionar la mayor cantidad de información que sea relevante para el objeto de estudio.
- Proporcione una descripción completa del dataset: el dataset está compuesto por 29224 filas y 287 columas, tipos de datos: flotantes y enteros. para poder analizar el trabajo de investigación se filtro por provincia teniendo un total de 321 filas y 287 columnas de Tierra del Fuego

------------

### Organizacion del Repositorio
    
    ├── LICENSE
    ├── Makefile           <- Makefile con comandos como `make data` o `make train`
    ├── README.md          <- El README del nivel superior para desarrolladores o usuarios de este proyecto.
    ├── data
    │   ├── external       <- Datos de fuentes externas.
    │   ├── interim        <- Datos intermedios que han sido transformados.
    │   ├── processed      <- Datasets finales para el modelado.
    │   └── raw            <- Datos crudos internos.
    │
    ├── docs               <- Un proyecto Sphinx por defecto, vea sphinx-doc.org para mas detalles.
    │
    ├── models             <- Modelos entrenados, predicciones o resumenes de modelos.
    │
    ├── notebooks          <- Jupyter notebooks. La convencion para            		nombrarlos es un
    │                                    numero (para ordenarlos) seguido de las iniciales del creador y una descripcion corta 
    │                                   demilitada por "-" por ejemplo `1.0-jqp-exploracion-inicial-datos`.
    │
    ├── references         <- Diccionario de datos, manuales y otro material explicativo.
    │
    ├── reports            <- Analisis generado como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Graficos y figuras generadas para ser usadas en reportes.
    │
    ├── requirements.txt   <- El archivo de requerimientos para reproducir el ambiente de analisis por ejemplo
    │                         generado con `pip freeze > requirements.txt`
    │
    ├── setup.py           <- hace el proyecto instalable mediante pip  (pip install -e .) asi src puede ser importado. can be imported
    ├── src                <- Codigo fuente usado en este proyecto.
    │   ├── __init__.py    <- Hace a src un modulo de Python
    │   │
    │   ├── data           <- Scripts para descargar o generar los datos.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar los datos crudos en features para el modelado.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para entrenar modelos y luego hacer predicciones.
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear visualizaciones orientadas a la exploracion de datos o a los resultados.
    │       └── visualize.py
    │
    └── tox.ini            <- archvi tox con ajustes para ejecutar tox; vea tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
