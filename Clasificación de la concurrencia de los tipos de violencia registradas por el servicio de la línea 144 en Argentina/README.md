Linea144
==============================

## Clasificación de la concurrencia de los tipos de violencia registradas por el servicio de la línea 144 en Argentina
### Tema
Clasificación de las violencias registradas en la línea 144 de orientación frente a situaciones de violencia de género.

### Objetivo
Clasificar mediante modelos de aprendizaje no supervisado, la co ocurrencia de los diferentes tipos de violencia de género por los que se
recurre a la línea 144.

### Objetivo alternativo
Realizar la clasificación geográfica de las denuncias para indagar si hay una influencia en la región con la cantidad de denuncias recibidas

### Contexto del problema 
Dado el retroceso nacional en materia de políticas públicas de atención a las violencias, me parece relevante conocer el
comportamiento de la co ocurrencia de los diferentes tipos de violencias hacia las mujeres para identificar posibles estrategias locales
para la atención a las mismas. En caso de no poder realizar la clasificación por tipo de violencia, también es interesante abordar la
distribución geográfica para poder observar de qué manera se podría ir identificando regiones en las que se denuncia/denunciarán
situaciones de violencia de género.

### Fuentes
Los datos con los que se trabajará son los obtenidos en la página datos.gob.ar En la “Base de datos de la línea 144” que posee registro de
   todos los llamados realizados en el periodo 2020-2023


-----------------------
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- ....
    ├── README.md          <- README. 
    ├── data
    │   ├── external       <- Data from third party sources. Datos de fuentes externas.
    │   ├── interim        <- Intermediate data that has been transformed. Data intermedia transformada.
    │   ├── processed      <- The final, canonical data sets for modeling. Set de datos final para la modelización. 
    │   └── raw            <- The original, immutable data dump. Data original en archivo csv.
    │
    ├── docs               <- Documents explaining objetives. Documentos descriptivos del proyecto.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries. Modelos realizados
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials. Manuales de códigos.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. Reporte final. (EN DESARROLLO)
    │   └── figures        <- Generated graphics and figures to be used in reporting. Gráficos de reporte.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment. Requerimientos para la reproducción del modelo. (EN DESARROLLO)
    │
    ├── setup.py           <- ...
    ├── src                <- ....
    │   ├── __init__.py    <- ...
    │   │
    │   ├── data           <- ...
    │   │   └── make_dataset.py 
    │   │
    │   ├── features       <- ...
    │   │   └── ...
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 classification 
    │   │  
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- ...


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
