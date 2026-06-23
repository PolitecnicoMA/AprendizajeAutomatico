![Alt text](image.png)
## TECNICATURA SUPERIOR EN CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL
## APRENDIZAJE AUTOMATICO
### Profesor Lic. Martin Mirabete
### Alumna: Demari Monica Valeria
# Optimizacion de la Clasificacion y Asignacion de Docentes en Tierra del Fuego utilizando Aprendizaje Automatico

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

El proyecto consiste en optimizar la asignacion y clasificacion de aspirantes inscriptos para ejercer la docencia en el nivel secundario en la educacion secundaria mediante el analisis de datos.
### Desarrollo
 #### 	Descripcion del Proyecto
En este proyecto propongo la implementación de un modelo de aprendizaje automático para optimizar la asignación y clasificación de docentes en el nivel secundario. Ante la creciente disponibilidad de datos y la heterogeneidad en la formación académica de los aspirantes, buscaré automatizar y mejorar la eficacia y equidad de este proceso.
#### •	Objetivo General:
El objetivo central de este proyecto es desarrollar un modelo de aprendizaje automático capaz de automatizar y optimizar el proceso de clasificación de los aspirantes inscriptos para ejercer la docencia en el nivel secundario. La clasificación se realizará en las categorías de "Docente", "Habilitante" y "Suplente", tomando como base los títulos académicos y otros atributos relevantes presentes en el conjunto de datos proporcionado por la Junta de Clasificación de Educación Secundaria, y que a su vez proporcione recomendaciones predictivas sobre el espacio curricular más adecuado para cada docente, en base a su formación académica.
#### • Objetivos Específicos:
•	Predecir la clasificación docente ("Docente", "Habilitante" o "Suplente") según su título, institución emisora y provincia.
•	Determinar qué espacios curriculares son los más apropiados para cada docente.
•	Identificar relaciones y patrones ocultos entre la formación académica y la asignación curricular.
•	Sugerir recomendaciones alternativas de asignación curricular.

#### •	Contexto del problema y su relevancia
Actualmente, el proceso de clasificación de aspirantes para la Junta de Clasificación y Disciplina de Educación Secundaria, crucial para la asignación de espacios curriculares y cargos, se realiza de forma manual. Esto lo hace propenso a errores humanos y consume una considerable cantidad de tiempo y recursos.
A pesar del desarrollo en curso de un sistema de merituación por parte de los referentes informáticos, como estudiante considero una oportunidad significativa para aplicar técnicas de aprendizaje automático a los datos históricos de inscripción. La implementación de un modelo de aprendizaje automático es altamente relevante, ya que una mejor asignación puede determinar:
•	Mayor precisión, es decir que reduce la probabilidad de errores en la clasificación, garantizando una asignación docente más justa y eficiente.
•	Mayor eficiencia: La automatización del proceso acelerará la clasificación de aspirantes, liberando a los miembros de la Junta para otras tareas críticas.
•	Análisis predictivo: El modelo puede generar insights valiosos sobre la demanda de docentes en distintas áreas, facilitando la toma de decisiones estratégicas para la planificación e implementación de nuevas modalidades educativas.

#### •	Tipo de Problema y Modelos de ML
El problema principal es de clasificación: la variable objetivo es caracter, con clases "D" (Docente), "H" (Habilitante), "S" (Supletorio). También puede expandirse a un problema de recomendación (opcional en versiones futuras del proyecto). Para ello, como opción podría usar Modelos de regresion logistica, o Random Forest, como así también SVM (Support Vector Machine).

## Estructura del Proyecto
El proyecto sigue una estructura organizada en carpetas, diseñada para almacenar y procesar los datos de manera eficiente. A continuación se describe la organización principal del repositorio:

| Carpeta                       | Archivo                                                   | Descripción                                                 |
|-------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
|    Data                       | `Readme`                                                  | Estructura de la carpeta "data"                             |
|    Data/Raw                   | `dataset_jcyd_ok.xlsx`                                    | Dataset original                                            |
|    Data/processed             | `dataset_docentes_etl.csv`                                | Dataset procesado                                           |  
|    docs                       | `README.md`                                               | Enlace del video                                            |
|    docs/docs                  | `README.md`                                               | Informe final                                               |
|    docs/docs                  | `A-FORO -Dominios de interés para el parcial.pdf`         | Documento PDF informado en Foro del campus                  |
|    docs/docs                  | `B-Entrega 1- Descripción y Formulación del Objetivo.pdf` | Documento PDF presentado en el campus                       |
|    docs/docs                  | `C-Entrega 2- Descripción del Dataset y Origen.pdf`       | Documento PDF ipresentado en el campus                      |
|    docs/docs                  | `README_Entrega_2.md `                                    | Descripción del Dataset y Origen                            |
|    noteooks                   | `Readme`                                                  | Estructura de la carpeta "notebook"                         |
|    noteooks                   | `1-Descripción del dataset.ipynb`                         | Acceso y descripción completa del dataset                   |
|    noteooks                   | `2-Limpieza y Tratamiento de Datos .ipynb`                | Proceso ETL                                                 |
|    noteooks                   | `3-Modelo_Regresion_Logistica.ipynb`                      | Notebook con modelo de Regresion Logística y visualizaciones|
|    noteooks                   | `4-Arbol_Decision.ipynb`                                  | Notebook con modelo de árbol de decisión                    |
|    noteooks                   | `5-Modelo_Random_Forest.ipynb`                            | Notebook con modelo Random forest                           |
|    noteooks                   | `6-Regresion_Logistica_Por_Espacio_Poco_Dato .ipynb`      | Notebook de regresión aplicada a espacios con pocos datos   |


## Video del proyecto

https://drive.google.com/file/d/1CqgWpa99TKnsqTO8opnmHb-owzpIfHCO/view?usp=sharing

## Project Organization

```
├── LICENSE            <- Licencia de código abierto si se elige una
├── Makefile           <- Makefile con comandos de conveniencia como `make data` o `make train`
├── README.md          <- README de nivel superior para desarrolladores que utilizan este proyecto..
├── data
│   ├── external       <- Datos de fuentes de terceros.
│   ├── interim        <- Datos intermedios que han sido transformados
│   ├── processed      <- Los conjuntos de datos finales y canónicos para modelado.
│   │      └── dataset_docentes_etl.csv       <- Archivo csv limpio para el posterior modelo de machine learning.
│   └── raw            <- Documento original e inmutable de datos
│   │      └── dataset_jcyd_ok.xlsx           <- Archivo excel con los datos de aspirantes inscrptos en la JCYDES.
│
├── docs               <- Documentacion del proyecto; ver www.mkdocs.org para más detalles
│
├── models             <- Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos
│
├── notebooks          <- Notebooks de Jupyter. La convención de nombres es un número (para ordenar),
│                         las iniciales del creador y una breve descripción delimitada por guiones, por ejemplo,
│                         `1.0-jqp-exploración-inicial-de-datos`.
│
├── pyproject.toml     <- Archivo de configuración del proyecto con metadatos del paquete para 
│                         Clasificacion_Asignacion_DocentesTDF y configuración para herramientas como black.
│
├── references         <- Diccionarios de datos, manuales y otros materiales explicativos.
│
├── reports            <- Análisis generado como HTML, PDF, LaTeX, etc.
│   └── figures        <- Gráficos y figuras generados para ser utilizados en informes
│
├── requirements.txt   <- Archivo de requisitos para reproducir el entorno de análisis, por ejemplo,
│                         generado con `pip freeze > requirements.txt`
│
├── setup.cfg          <- Archivo de configuración para flake8
│
└── Clasificacion_Asignacion_DocentesTDF   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes Clasificacion_Asignacion_DocentesTDF a Python module
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

