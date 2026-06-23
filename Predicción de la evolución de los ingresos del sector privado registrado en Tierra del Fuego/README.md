# Tecnicatura Superior en Ciencia de Datos e IA - Politécnico Malvinas Argentinas - 2025  
## Aprendizaje Automático  
**Profesor:** Martín Mirabete  
**Alumna:** Ventura Stella Maris

# 📈 Predicción de la evolución de los ingresos del sector privado registrado en Tierra del Fuego  

---

## 🧩 Descripción del Proyecto  
Este proyecto aplica **Aprendizaje Automático** para analizar la evolución de los ingresos del sector privado registrado en **Tierra del Fuego**, una provincia con características económicas particulares.  

Dada la alta inflación y el impacto del costo de vida en la región, el objetivo es desarrollar un modelo predictivo que permita **estimar la remuneración promedio** y su relación con la **Canasta Básica Total (CBT) y el endeudamiento de los hogares**.

---

## 🎯 Objetivos  

### Objetivo general  
Desarrollar un **modelo de regresión supervisada** que prediga el nivel de consumo con tarjeta de crédito a partir de la evolución mensual de los ingresos y la inflación.  

### ✅ Objetivos específicos  
- Limpieza y transformación de la serie histórica de ingresos por rama de actividad.  
- Integración de datos complementarios como CBT e indicadores de endeudamiento.  
- Aplicación de modelos de regresión (Lineal, Árboles de Decisión, Random Forest, etc.).  
- Evaluación del modelo con métricas como MAE, RMSE y R².  
- Análisis del poder adquisitivo en relación al ingreso y la inflación.

---

## 📂 Fuentes de Datos  
Este proyecto utiliza fuentes públicas y oficiales:  
- **Banco Central de la República Argentina (BCRA)** → Datos de pagos minoristas y crédito.  
- **IPIEC** → Ingresos del sector privado registrado por actividad.  
- **INDEC** → IPC y evolución de precios por categoría.  

Los datos fueron sometidos a procesos de **limpieza, transformación y normalización**, y se encuentran organizados en carpetas según el estado de procesamiento.

---

## 🛠️ Tecnologías Utilizadas  
El desarrollo se realizó íntegramente en **Python**, utilizando:

- `pandas` y `numpy` para manipulación de datos  
- `matplotlib` y `seaborn` para visualización  
- `scikit-learn` para entrenamiento de modelos  
- `jupyter notebook` para análisis exploratorio  
- `git` y `GitHub` para control de versiones  
- `cookiecutter` para estructuración del proyecto  
## 🎬 video explicativo: https://drive.google.com/file/d/1rCC8R_5zC9tYD0iV0d8Q4ot71ZB6CJYB/view?usp=drive_link
📌 Nota: el modelo de aprendizaje automático se encuentra en la carpeta models.
---

## 🧱 Estructura del Repositorio (estilo Cookiecutter)

```plaintext
├── LICENSE
├── Makefile               <- Comandos automatizados como `make data`
├── README.md              <- Este archivo
│
├── data/
│   ├── external/          <- Datos de fuentes externas
│   ├── interim/           <- Datos intermedios procesados parcialmente
│   ├── processed/         <- Datos finales para modelado
│   └── raw/               <- Datos crudos originales
│
├── docs/                  <- Documentación técnica adicional
│
├── models/                <- Modelos entrenados, serializados o evaluaciones
│
├── notebooks/             <- Jupyter notebooks
│                            Ej: 1.0-smv-exploracion-inicial.ipynb
│
├── references/            <- Fuentes externas, papers, artículos
│
├── reports/
│   └── figures/           <- Gráficos y visualizaciones generadas
│
├── requirements.txt       <- Dependencias del proyecto
├── setup.py               <- Permite importar `src` como módulo
├── tox.ini                <- Configuración para testeo con tox
│
├── src/
│   ├── __init__.py        <- Define `src` como paquete
│   ├── data/
│   │   └── make_dataset.py         <- Limpieza y organización de datos
│   ├── features/
│   │   └── build_features.py       <- Ingeniería de variables
│   ├── models/
│   │   ├── train_model.py          <- Entrenamiento
│   │   └── predict_model.py        <- Predicción
│   └── visualization/
│       └── visualize.py            <- Gráficos y visualizaciones
