**COVID-19 - Predicción de cantidad diaria de nuevas dosis de vacunas en Tierra del fuego**

**Objetivo General**

Desarrollar un modelo de Aprendizaje Automático que permita predecir predecir cuántas dosis de vacunas se aplican por día en Tierra Del Fuego, usando datos climáticos, de movilidad y temporales.

**Objetivos Específicos**

- Preprocesar los datos de vacunación, movilidad y clima.
- Construir un modelo de regresión supervisada para predecir la variable `new_vaccine_doses_administered`.
- Evaluar el rendimiento de distintos algoritmos de regresión (Regresión Lineal, Random Forest, SVR).
- Analizar la importancia relativa de cada variable en la predicción.
- Aplicar el modelo sobre datos futuros para anticipar variaciones estacionales y asistir la planificación sanitaria.

**Contexto y Relevancia**

Durante y después de la pandemia del COVID-19, el seguimiento de las campañas de vacunación se ha convertido en una herramienta clave para los sistemas de salud.

Prever cuántas dosis se aplicarán diariamente, en función de factores como el clima, la movilidad o la época del año, permite:

- Organizar mejor los recursos.
- Optimizar la logística de distribución.
- Priorizar zonas de mayor demanda.
- Focalizar estrategias de comunicación sanitaria.

Este proyecto se enfoca en Argentina, Tierra Del Fuego, utilizando:

- Variables climáticas: temperatura, precipitación, humedad.
- Variables de movilidad: hacia lugares de trabajo y en el hogar.
- Variables temporales: mes y año.
- Datos históricos de vacunación.

**Tipo de Problema**

Regresión Supervisada  
Se busca predecir una variable continua (`new_vaccine_doses_administered`) en función de un conjunto de características independientes.

**Modelos de Aprendizaje Automático Considerados**

- Regresión Lineal Múltiple: modelo base por su sencillez e interpretabilidad.
- Random Forest Regressor: robusto ante relaciones no lineales y valores atípicos.
- Support Vector Regressor (SVR): útil para capturar relaciones no lineales con kernel RBF.

**Estructura del Proyecto**
**Estructura del Proyecto**
```
├── data/                # Datos originales y derivados
│   ├── raw/             # Datos sin procesar (brutos)
│   ├── processed/       # Datos listos para el modelado
│   └── interim/         # Datos intermedios (transformaciones)
│
├── docs/                # Documentación del proyecto
│   ├── 1. Proceso del codigo realizado.pdf
│   └── 2. Informe del proyecto.pdf
│
├── models/              # Modelos entrenados y serializados
│
├── notebooks/           # Notebooks de análisis y entrenamiento
│   └── 2025_AA_Proyecto.ipynb
│
├── references/          # Artículos, papers o benchmarks usados como base
│
├── reports/             # Reportes y visualizaciones
│   ├── figures/         # Imágenes generadas
│   └── analisis_final/  # Evaluación de modelos
│
├── src/                 # Código fuente del proyecto
│   ├── preprocess/      # Scripts de limpieza y preparación de datos
│   ├── train/           # Scripts de entrenamiento
│   └── predict/         # Scripts de predicción con modelos entrenados
│
├── .gitignore           # Archivos y carpetas excluidos del control de versiones
├── LICENSE              # Licencia del proyecto
├── README.md            # Descripción general del proyecto
└── requirements.txt     # Dependencias necesarias para reproducir el entorno
```

Origen del Dataset

Fuente: https://health.google.com/covid-19/open-data/

Entidad recopiladora: Google y colaboradores académicos.

Cobertura geográfica: global, incluyendo datos específicos por país, provincia o región.

Proceso de recopilación: los datos son integrados desde múltiples fuentes oficiales de gobiernos, instituciones de salud pública, y datos abiertos de movilidad (Google Mobility), clima (NOAA), y vacunación (Our World in Data).

Preprocesamiento realizado:

Se filtraron los datos para un país específico (por ejemplo, Argentina).


Link Video:
[https://drive.google.com/file/d/1WOf4rLjNWLWCozGruRt-E5nZWLUnxOks/view?usp=sharing](https://drive.google.com/file/d/1f-AgKG7lYziEbn4FAgULoIM16gjYq2u4/view?usp=sharing)

Gabriela Velasquez
Proyecto final - Aprendizaje Automático 2025

