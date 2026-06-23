![Portada Politec](img/PORTADA_POLITEC.png)

---

**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial  
**Institución:** Politécnico Malvinas Argentinas  
**Materia:** Aprendizaje Automático

**Proyecto:** Predicción de Producción Sostenible de Trucha en Tierra del Fuego

- **Alumno:** Nicolás Cussi
- **Profesor:** Martín Mirabete

---
## Recursos Multimedia
- [Explicación del proceso - Google Drive](https://drive.google.com/file/d/1uRB9-RXwKAGeWrpzWsQlMKK_idP88cNL/view?usp=sharing)

---
Predicción de Producción Sostenible de Trucha en TDF mediante Modelos de Aprendizaje Automático
==============================

El presente proyecto se enmarca en la aplicación de técnicas de Aprendizaje Automático para apoyar la toma de decisiones en la acuicultura de trucha arcoíris en la provincia de Tierra del Fuego, Antártida e Islas del Atlántico Sur, Argentina. La trucha es una de las especies acuícolas más cultivadas del país, y aunque su producción en Tierra del Fuego representa un porcentaje menor del total nacional, se reconoce un alto potencial de desarrollo gracias a las condiciones naturales privilegiadas que ofrece la provincia: aguas frías, limpias y con alta concentración de oxígeno.

# Descripción del Proyecto

Este proyecto desarrolla modelos de aprendizaje automático para **predecir el nivel de producción** y **clasificar condiciones favorables o críticas** para la acuicultura de trucha en Tierra del Fuego, utilizando datos históricos oficiales (MAGyP, SENASA, registros de temperatura del Canal Beagle).

---

## Variables Utilizadas

- **Producción histórica anual** de trucha por provincia (toneladas)
- **Movimientos logísticos** de alevinos y adultos (ingresos y egresos)
- **Temperatura superficial del agua** (promedio mensual/anual)
- **Estacionalidad**
- **Año (temporal)**
- **Cambios normativos** y **eventos climáticos extremos** (opcional)

---

## Objetivo del Trabajo

### Objetivo General
> Desarrollar modelos de aprendizaje automático para predecir y clasificar el nivel de producción acuícola de trucha en Tierra del Fuego, optimizando la planificación y fomentando una producción sostenible y eficiente.

### Objetivos Específicos

- Identificar las variables que más impactan en la producción anual de trucha en Tierra del Fuego.
- Aplicar modelos de regresión para estimar la producción anual (toneladas) en función de variables logísticas y ambientales.
- Aplicar modelos de clasificación para identificar condiciones productivas **“favorables”** o **“críticas”** para la acuicultura local.
- Evaluar el rendimiento de los modelos mediante métricas como **MAE**, **RMSE**, **precisión**, **recall** y **F1-score**.
- Contribuir con una herramienta analítica útil para organismos provinciales y productores locales.

---

## Contexto y Relevancia

La acuicultura en Tierra del Fuego es una actividad con gran potencial pero enfrenta desafíos importantes:

- **Ventajas:** Criaderos como el de Puerto Almanza aprovechan un ambiente natural ideal.
- **Desafíos:**  
  - Logística insular limitada  
  - Condiciones climáticas cambiantes  
  - Ausencia de herramientas predictivas para la toma de decisiones

**Beneficios de aplicar IA:**

- Anticipar escenarios productivos antes del ciclo de engorde
- Optimizar el ingreso de alevinos
- Establecer calendarios productivos según condiciones ambientales
- Proveer base técnica para regulaciones acuícolas

Además, el cambio climático hace que pequeñas variaciones en la temperatura del agua impacten fuertemente en la producción y el metabolismo de la trucha.

---

## Tipo de Problema y Modelos a Utilizar

- **Regresión:**  
  - *Objetivo:* Predecir la cantidad de producción anual (toneladas)
  - *Modelos sugeridos:*  
    - Regresión lineal múltiple  
    - Random Forest Regressor  
    - Gradient Boosting Regressor

- **Clasificación:**  
  - *Objetivo:* Clasificar si un año será **“favorable”** o **“crítico”** para la producción de trucha
  - *Modelos sugeridos:*  
    - Random Forest Classifier  
    - SVM  
    - K-Nearest Neighbors (KNN)  
    - Logistic Regression (baseline)

---

## En Síntesis

Este proyecto aplica técnicas de **inteligencia artificial** a un problema real y estratégico de la región. El desarrollo de modelos predictivos permitirá anticipar y optimizar la producción acuícola, aportando valor práctico e innovación para productores y organismos locales.  
Los modelos serán entrenados para identificar patrones significativos en los datos históricos, superando el análisis de simples promedios.

---


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
