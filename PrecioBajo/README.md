# *Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial* 
# *Politécnico Malvinas Argentinas.*

------------

## Aprendizaje Automático
Estudiante: Nahuel Constenla.

------------

# PrecioBajo
Trabajo Final de Aprendizaje Automatico - Pedicción de Precios - Cortes de Carnes
"Utilizaremos Técnicas de Aprendizaje Automatico, que fuimos conociendo a lo largo del recorrido de la Materia, de predecir el Aumento de Precios de Cortes de la carne mediante clasificación.*

------------

#### Entrega 1 - 03/06/2024

Definición del problema será el de abordar el problema de predicción de precios futuros de los productos de la Carne en base al DataSet disponible de una plataforma de Precios a Nivel Provincial.

##### Este proyecto de Aprendizaje Automático se va a centra en responder a la siguiente pregunta de investigación e Hipótesis:

•	¿Cuáles son los factores más influyentes que determinan los precios de los productos de la Carne en la Ciudad de Río Grande?
•	“¿Es posible predecir con precisión la variabilidad en los Futuros Precios de los Productos de la Carne que la población de Rio Grande consume?”

Factores como el costo de los combustibles que las Empresas de Transportes trasladan al servicio que prestan, el Alimentos para que se provee a los animales, las condiciones climáticas zonales, las políticas Impositivas Nacionales como Provinciales, las tasas al cambio, son algunas de las influencias significativas que afectan a los precios locales de los productos de la carne.
La relevancia de este problema también se acentúa en el contexto de la globalización y el comercio internacional, donde los precios locales pueden verse afectados por eventos en otras partes del país y el mundo, como pandemias, conflictos geopolíticos y cambios en las políticas comerciales.

#### Objetivo

El objetivo principal de este proyecto es desarrollar un modelo de Aprendizaje Automático capaz de predecir los precios futuros de productos de la Carne a nivel local. La predicción precisa de estos precios puede proporcionar a las Vecinas y Vecinos de la Ciudad de Río Grande, una ventaja significativa en la toma de decisiones a la hora de planificar una compra Semanal o Mensual. Específicamente, el proyecto se centrará en predecir los precios de diferentes tipos de carnes como Asado, Vacío, tipos de Carne Picada, Etc. utilizando datos históricos y diversas variables que puedan influir en los precios.

#### Problema a Abordar

El problema que este proyecto pretende abordar es la volatilidad y fluctuación de los precios en los Comercios Locales de los productos de la carne en el mercado de la Ciudad de RG. Estos cambios pueden deberse a una variedad de factores, incluyendo cambios en los costos de producción, variaciones estacionales, en la demanda, políticas de impuestos, entre otros. 
La capacidad de prever estas variaciones puede ayudar a mitigar riesgos y optimizar bolsillos de los Vecinos y Vecinas de la Ciudad.

#### Selección Del Modelo

Utilizare un modelo de regresión de Aprendizaje Supervisado, probaremos con un modelo de regresión lineal (LinearRegression), ya que intentaremos predecir valore en este caso precios a futuro de una o más variables.
También desarrollaremos un modelo de Árbol de Decisión (RandomForestRegressor) para mejorar la precisión y la robustez de las predicciones

#### Pasos A Seguir

1.- Carga de Librerías necesarias
•	Pandas
•	Numpy
•	Seaborn
•	Matplotlib
•	sklearn

2.- Exploración de Datos
•	Análisis General del DataSet
•	Análisis Descriptivo y Estadístico del DataSet
•	Análisis de valores nulos y duplicados.

3.- Preprocesamiento
•	Conversión de fechas a un formato adecuado 
•	Codificación de variables categóricas.
•	Normalización o estandarización de precios.

4.- Modelado
•	Definición del problema (Predicción de precios futuros, clasificación de productos o análisis de tendencias).
•	Selección de algoritmos apropiados (Regresión, Clasificación).
•	Entrenamiento y validación del Modelo.

5.- Evaluación
•	Métricas de desempeño para evaluar la precisión del modelo.
•	Interpretación de resultados y conclusiones.

------------

#### Organizacion del Repositorio
    
    ├── LICENSE
    ├── Makefile           <- Makefile con comandos como `make data` o `make train`
    ├── README.md          <- # Descripción del Proyecto de Apendizaje Automatico 
    ├── data
    │   ├── external       <- Datos de fuentes externas.
    │           └──                 <- # DataSet "Carnes.csv"
    │ 
    │   ├── interim        <- Datos intermedios que han sido transformados.
    │   ├── processed      <- Datasets finales para el modelado.
    │   └── raw            <- Datos crudos internos.
    │
    ├── docs               <- Un proyecto Sphinx por defecto, vea sphinx-doc.org para mas detalles.
    │
    ├── models             <- Modelos entrenados, predicciones o resumenes de modelos.
    │
    ├── notebooks          <- Jupyter notebooks.  
    │                               <- # Archivo "Examen_Parcial_Final.ipynb" - Proyecto Final              
    │
    ├── references         <- Diccionario de datos, manuales y otro material explicativo.  
    │                               <- # Archivo "Origen y Descripción del DataSet.md" - Informe del Analisis del DataSet
    │
    ├── reports            <- Analisis generado como HTML, PDF, LaTeX, etc.
    │                               <- Entrega Punto N° 1.md
    │                               <- Reporte de Resultados.md
    │ 
    │   └── figures        <- Graficos y figuras generadas para ser usadas en reportes.
    │                               <- Imagen_1.PNG - Imagen_2.PNG - Imagen_3.PNG - Imagen_4.PNG - Imagen_5.PNG - Imagen_6.PNG
    │                               <- RegresionLineal.PNG - ArbolD2.PNG
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