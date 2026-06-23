## Link Video Explicativo: https://drive.google.com/file/d/10ph50rfSoksVY4EXShnETB_HtHaaxmor/view?usp=sharing

![Gas](https://github.com/user-attachments/assets/191ee540-9b02-43f1-9dd9-8c7f95c6ca0d)

![banner_flat1](https://github.com/user-attachments/assets/81259883-b2bd-4db5-bf90-547c8d3d96af)

## MATERIA: APRENDIZAJE AUTOMÁTICO
## DOCENTE: LIC. MARTÍN MIRABETE
## ALUMNO: DIEGO ORONÁ
## TÍTULO DEL PROYECTO: CONSUMO DE GAS NATURAL POR RED SEGÚN TIPO DE USUARIO EN TIERRA DEL FUEGO.

## Descripción del Proyecto:
El proyecto “Consumo de Gas Natural por red según tipo de usuario en Tierra del Fuego” tiene como propósito analizar cómo se consume el gas natural en la provincia, dividiendo los datos según el tipo de usuario, que incluye hogares, comercios e industrias. Se recogerán datos sobre el consumo, la facturación y estadísticas de uso, los cuales serán limpiados y transformados para facilitar su análisis. Mediante técnicas de aprendizaje automático, se buscarán patrones en estos datos y se realizarán proyecciones sobre el consumo futuro, teniendo en cuenta factores como el clima y el crecimiento de la población.

## Objetivo del Proyecto:
El objetivo del proyecto es abordar el problema de cómo consumir gas natural de manera eficiente en la provincia de Tierra del Fuego, ya que la demanda varía mucho entre los diferentes tipos de usuarios, como hogares, comercios e industrias. Mediante un modelo de aprendizaje automático, se buscará identificar patrones en el consumo de gas, lo que permitirá anticipar la demanda futura y mejorar la gestión de la red de distribución. Este enfoque es fundamental para enfrentar retos como la planificación de la infraestructura, la asignación adecuada de recursos y asegurar un suministro constante y sostenible, lo que ayuda a reducir el riesgo de desabastecimiento y a mejorar la calidad del servicio.

## Contexto:
El proyecto sobre el consumo de gas natural en Tierra del Fuego se sitúa en una provincia que ha visto un notable crecimiento en su población y economía en los últimos años. Este incremento en la demanda de gas natural, impulsado por el aumento de hogares, comercios e industrias, presenta importantes desafíos para la gestión de la red de distribución. La variabilidad en el consumo entre los diferentes tipos de usuarios hace que la planificación y el suministro sean aún más complicados.

## Relevancia:
Es fundamental abordar este problema para garantizar un suministro de gas que sea adecuado y sostenible. Si la demanda sigue creciendo sin control, podría haber escasez de recursos, lo que afectaría la calidad del servicio y tensaría la infraestructura existente. Además, con el cambio climático y la evolución en los patrones de consumo, es vital contar con datos precisos y proyecciones que permitan anticipar la demanda futura.

## Preguntas de Investigación:
¿Cómo varía el consumo de gas natural entre los diferentes sectores (Comercial, Residencial, Industrial)?

¿Existen patrones estacionales en el consumo de gas natural?

¿Cómo impacta la población de cada sector en el consumo de gas natural?

¿Se pueden predecir los patrones de consumo futuro en función de los datos históricos?

## Descripción del Dataset:
El dataset utilizado contiene “cuatro hojas: índice, anual, mensual y ficha técnica” y “la hoja Anual contiene 9 características, mientras que la hoja Mensual contiene 10 características”, incluyendo que “en la hoja anual, la mayoría de las columnas son de tipo categóricos, excepto una columna de tipo numérico y en la hoja mensual similarmente, la mayoría de las columnas son de tipo categóricos, con una columna de tipo numérico”. Los datos provienen de “ENARGAS Ente Nacional Regulador del Gas”, adquiridos de los “años 1993-2023”, y se ha realizado el siguiente preprocesamiento: “Carga del archivo y exploración de los datos, limpieza de los datos, eliminación de las solapas “Indice”, “Mensual” y “Ficha Técnica”, rellenar valores nulos, eliminar columnas, cambiar nombres de las columnas, eliminar filas y eliminar valores atípicos”.

## Desarrollo del Modelo:
El modelo desarrollado incluye una arquitectura basada en “Regresión Lineal Múltiple”, utilizando los algoritmos de “Método de Mínimos Cuadrados”. Los hiperparámetros se ajustaron de la siguiente manera: “Se cargaron los datos y se definieron las variables independientes y dependientes. Se dividieron los datos 80% entrenamiento y 20% prueba y se entrena el modelo de regresión lineal múltiple”. Las métricas de evaluación obtenidas fueron: “Error Cuadrático Medio (MSE): El valor de 0.6732 indica que, en promedio, las predicciones del modelo difieren de los valores reales por aproximadamente esa cantidad en la escala de la variable objetivo. En este caso, el valor es relativamente bajo, lo que sugiere que el modelo tiene una buena capacidad de predicción. Coeficiente de Determinación (R²): Un valor de 0.9889 indica que el modelo es capaz de explicar el 98.89% de la variación en los datos” y otras métricas relevantes son los “coeficientes del modelo, Comerciales: 0.000126. Residenciales: 0.000084. Industriales: -0.000195. Los sectores Comerciales y Residenciales tienen un impacto positivo en la variable dependiente (años, consumo total, o lo que estés modelando), aunque el impacto comercial es ligeramente mayor. El sector Industrial tiene un impacto negativo, lo que podría reflejar una dinámica más volátil o menos predecible en este sector”.

## Análisis de Resultados:
El análisis exploratorio de datos reveló “Sectores comerciales y residenciales muestran una tendencia de crecimiento consistente en el consumo a lo largo de los años, mientras que industriales presenta mayor variabilidad. Esto podría implicar que los sectores comerciales y residenciales tienen una demanda de gas más predecible y en aumento continuo, mientras que el sector industrial podría estar influenciado por factores más dinámicos, como la producción industrial”. Las conclusiones claves de este análisis son “que mientras los sectores comerciales y residenciales presentan una demanda de gas más estable y creciente, el sector industrial exhibe un comportamiento más volátil, influenciado por factores económicos y productivos”. Los resultados del modelo indican que “el consumo de gas natural entre los diferentes sectores (Comercial, Residencial e Industrial)” varia por patrones estacionales y de producción. En los sectores residenciales y comerciales el consumo de gas impacta directamente en la población, y que se pueden predecir consumos futuros en función de los datos históricos” (respondiendo a las preguntas de investigación). Se ha concluido que “los negocios y las casas usan gas de manera bastante predecible y cada vez más con el paso del tiempo. Es como si siguieran un patrón constante. En cambio, las fábricas son más irregulares en su consumo de gas - un mes pueden usar mucho y al siguiente mucho menos, principalmente porque depende de cuánto estén produciendo y cómo va la economía en general.”

## Conclusión:
En conclusión, el modelo desarrollado ha sido efectivo en la “predicción de consumos futuros para garantizar la demanda de gas en cada sector de la Provincia de Tierra del Fuego.
* El modelo predice que el consumo comercial para el año 2024 será de aproximadamente 83,129 m3 unidades de gas.
* El modelo predice que el consumo residencial de gas en 2024 será de aproximadamente 417,902 m3 unidades de gas.
* El modelo predice que el consumo industrial de gas en 2024 será de aproximadamente 20,831 m3 unidades de gas”.
Para futuros trabajos, se recomienda “Implementar variables de, aumento demográfico y temperaturas promedio en la Provincia de Tierra del Fuego”.

## ABSTRACT
## This study investigates the effectiveness of a machine learning model for predicting natural gas consumption in Tierra del Fuego, which is segmented by user type. The model is trained using historical consumption data, including variables such as weather conditions, user type, and consumption patterns. The results demonstrate that the model can predict gas consumption with a high degree of accuracy. Furthermore, this approach may enhance operational efficiency and optimize resource planning, providing benefits for both gas providers and consumers. It is expected that these findings will contribute to more sustainable practices in the energy sector. Additionally, the analysis was conducted thoroughly to ensure reliable outcomes.
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
