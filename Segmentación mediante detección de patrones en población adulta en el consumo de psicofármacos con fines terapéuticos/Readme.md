# PROYECTO DE APRENDIZAJE AUTOMÁTICO

# Segmentación mediante detección de patrones en población adulta en el consumo de psicofármacos con fines terapéuticos

## Descripción

El presente proyecto tiene como objetivo identificar patrones de consumo de psicofármacos en población adulta mediante técnicas de Aprendizaje Automático no supervisado.

A partir de la integración y procesamiento de diferentes conjuntos de datos provenientes de la encuesta Medical Expenditure Panel Survey (MEPS), se construyó un dataset consolidado que permite analizar características demográficas, socioeconómicas, clínicas y farmacológicas asociadas al consumo de medicamentos psicotrópicos.

El proyecto busca detectar perfiles diferenciados de individuos mediante técnicas de reducción de dimensionalidad y clustering, contribuyendo a una mejor comprensión de los patrones de utilización de psicofármacos con fines terapéuticos.

---

# Objetivo General

Identificar patrones de consumo de psicofármacos en población adulta mediante la aplicación de técnicas de Aprendizaje Automático no supervisado.

---

# Objetivos Específicos

- Integrar múltiples conjuntos de datos provenientes de la encuesta MEPS.
- Construir un dataset consolidado para el análisis del consumo de psicofármacos.
- Realizar análisis exploratorio de datos.
- Aplicar técnicas de reducción de dimensionalidad mediante PCA.
- Implementar algoritmos de clustering utilizando K-Means.
- Identificar perfiles diferenciados de consumo farmacológico.
- Interpretar los resultados obtenidos.

---

# Fuente de los Datos

Los datos utilizados provienen de la encuesta pública:

**Medical Expenditure Panel Survey (MEPS) – 2020**

Organismo responsable:

Agency for Healthcare Research and Quality (AHRQ)

Sitio oficial:

https://meps.ahrq.gov

Archivos utilizados:

- H224 – Full Year Consolidated Data File
- H222 – Medical Conditions File
- H229A – Prescribed Medicines File

---

# Dataset Final

El dataset final fue construido mediante la integración de tres conjuntos de datos pertenecientes a MEPS 2020.

Cada fila representa un individuo identificado mediante la variable DUPERSID.

## Características Generales

| Característica | Valor |
|---------------|---------|
| Registros | 27.805 |
| Variables | 18 |
| Unidad de análisis | Individuo |
| Formato | CSV |
| Tipo de problema | Aprendizaje No Supervisado |

---

# Diccionario de Variables

| Variable | Descripción |
|-----------|-------------|
| DUPERSID | Identificador único del individuo |
| AGE20X | Edad |
| SEX | Sexo |
| MARRY20X | Estado civil |
| EDUCYR | Años de educación |
| POVCAT20 | Categoría de ingresos |
| EMPST53 | Situación laboral |
| INSCOV20 | Cobertura médica |
| MNHLTH53 | Estado de salud mental |
| RTHLTH53 | Estado general de salud |
| RACETHX | Grupo racial o étnico |
| cantidad_condiciones | Número de condiciones médicas registradas |
| recetas_totales | Cantidad total de recetas |
| benzodiacepinas | Consumo de benzodiacepinas |
| antidepresivos | Consumo de antidepresivos |
| hipnoticos | Consumo de hipnóticos |
| ansioliticos | Consumo de ansiolíticos |
| total_psicofarmacos | Total de psicofármacos consumidos |

---

# Metodología

El proyecto fue desarrollado siguiendo las etapas clásicas de un flujo de trabajo de Ciencia de Datos:

1. Obtención de datos.
2. Limpieza y preparación.
3. Integración de datasets.
4. Construcción de variables derivadas.
5. Análisis exploratorio de datos.
6. Estandarización de variables.
7. Reducción de dimensionalidad mediante PCA.
8. Segmentación mediante K-Means.
9. Evaluación e interpretación de resultados.

---

# Modelos Utilizados

## Principal Component Analysis (PCA)

Utilizado para reducir la dimensionalidad del conjunto de datos conservando la mayor cantidad posible de información.

## K-Means Clustering

Utilizado para identificar grupos de individuos con patrones similares de consumo de psicofármacos.

---

# Estructura del Proyecto

El repositorio se encuentra organizado siguiendo los principios de la plantilla Cookiecutter Data Science.

```text
├── README.md

├── DATA
│   ├── RAW
│   │   ├── h224.csv
│   │   ├── h222.csv
│   │   └── h229a.csv
│   │
│   │
│   ├── PROCESSED
│   │   └── dataset_psicofarmacos_final.csv
|   |
├── Notebooks
│   ├── 01_unificacion_datos.ipynb
│   └── 02_modelo_clustering.ipynb

├── DOCS
|   ├── 01_Objetivos_y_Alcance del Proyecto.md
|   |
│   └── 02_Analisis_exploratorio.md
|
├── RPORTS
│   ├── FIGURES
│   │   ├── FIGURA 1.Distribucion de Edad de la Población Estudiada.png
│   │   ├── FIGURA 2_Distribución de Cantidad de Condiciones Médicas.png
│   │   ├── FIGURA 3_Consumo Total por Categoía Farmacológica.png
│   │   ├── FIGURA 4_Matriz de Correlación.png
│   │   ├── FIGURA 5_Método del Codo.png
│   │   ├── FIGURA 6_Visualización de Clusters en el Espacio PCA.png
│   │   ├── FIGURA 7_Cantidad de Individuos por Cluster.png
│   │   └── FIGURA 8_Promedio de Psicofármacos.png
│   │
│   └── 03_ Presentacion Final y Analisis de Resultados

├── models
│
└── requirements.txt
```

---

# Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook
- Git
- GitHub

---

# Principales Resultados

El análisis permitió identificar perfiles diferenciados de consumo de psicofármacos dentro de la población estudiada.

La aplicación de PCA facilitó la reducción de dimensionalidad y la visualización de la estructura de los datos, mientras que K-Means permitió segmentar a los individuos en grupos con características similares.

Los resultados sugieren que la complejidad clínica, la cantidad de recetas y el consumo de psicofármacos constituyen factores relevantes para la conformación de distintos perfiles de consumo.

---

# Repositorio Académico

Proyecto desarrollado para la asignatura Aprendizaje Automático.

Centro Politecnico Malvinas Argentinas

Año: 2026

Autora: Betiana Ruth Burgos
