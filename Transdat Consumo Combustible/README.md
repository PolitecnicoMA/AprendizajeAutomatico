

![340181243-0a9f62e9-2b2b-4cd4-8fcf-f4d4f3ad9ec4](https://github.com/user-attachments/assets/628b0a12-a8ec-4d30-bf61-bcda405b2607)


Transdat Consumo Combustible
==============================
Link video explicativo: https://drive.google.com/file/d/1qjwhRq6xX6HO8KJ7sXl74IQntTtly2ry/view?usp=sharing
--------------------------------
Abstract
------------
Automated Fuel Consumption Monitoring and Anomaly Detection Using Machine Learning
------------
This research project aims to develop a Machine Learning model capable of identifying whether vehicle fuel consumption is due to normal usage or other factors, such as fuel tank theft or tampering. The data is provided by the company Transdat, which implements remote data transmission solutions. One of the drawbacks is that when the engine turns off, the vehicle's computer stops collecting data until the engine is restarted. During these periods, the fuel level may differ from the last connection.The data obtained consists of reports from three different types of vehicles and was processed by type, as there is a significant difference in the amount of fuel consumed by a truck compared to a forklift or van, which could affect the model's accuracy when making classifications. The main objective of this project is to provide automated control over fuel tank tampering based on the reports obtained. 
-----------------------------

El siguiente proyecto para la materia Aprendizaje automático consta de desarrollar un modelo de ML el cual pueda ser capaz de reconocer si el gasto de combustible de los vehículos es producto del consumo normal, o de algún otro factor como sería el peor caso, el robo o la mala manipulación de los tanques de combustibles
-----------------
Objetivo del proyecto
------------------------------
Brindar un control automatizado sobre la manipulación de los tanques de
combustible, en base a los reportes obtenidos
=============================
*Contexto*
-----------------------------
Uno de los inconvenientes que se presentan es que a la hora de que el motor se apaga la
computadora del vehículo deja de recolectar datos hasta que se vuelve a poner en marcha el
motor. En esos lapsos el nivel de combustible puede presentar diferencias respecto a la última
conexión.
----------------------------
Hipótesis a contrastar:

Las diferencias que se encuentran en los registros de combustible da lugar a que se
sospeche de que haya una manipulación negativa sobre los tanques de combustibles.
(sustracción de combustible no autorizado)

------------------------------
Descripcion del Data Set y Origen 
-----------------------------
La descripcion detallada de los Data Sets Utilizados se encuentran en la carpeta docs. Visita este link para saber más https://github.com/mariagdc/Consumo_Combustible/tree/main/docs
-------------------------------
Desarrollo de los Modelos y conclusiones generales
* Furgoneta: el modelo que se ajusto perfectamente es el de Regresion Lineal: tieene un MSe de 0.08, un valor relativamente bajo- El r cuadrado es de 0.99 lo cual explicaria casi el 100% de la variabilidad de los datos de prueba. Haciendo predicciones kuy precisas y confiables
* Response.json(camion): En este caso ambos modelos Regresion Lineal y SVM funcionaron bien, sin embargo otra vez se ajusta mucho mejor el Modelo de Regresion Lineal. Ambos con un R cuadraro de  0.99, se diferencian en el MSE(error cuadratico medio) Regresion lineal con 119.84, y SVM con 910.70. Esto indica que las predicciones del modelo SVM son menos precisas y confiables.
* En el ultimo reporte (Xampi) Se deseaba predecir la cantidad de combustible a traves de los datos del tacometro del vehiculo ya que una vez explorado este data set nos encomtramos con datos faltantes que hicieron imposible el desarrollo de un buen modelo. Por ellos los siguientes datos no son nada precisos y muy poco confiables, por lo que no se puede realizar una interpretación positiva del modelo.   
--------------------------

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
