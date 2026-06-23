# Aprendizaje_Automatico_Parcial_2026

##  Predicción de Precios de Alquileres en Río Grande

### Autor

**Lionel Alfredo Martínez**
Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial

Link del video presentacion: https://youtu.be/I9ejc0LsFcc

---

# Descripción del Proyecto

Este proyecto desarrolla un modelo de Aprendizaje Automático orientado a la predicción de precios de alquileres en la ciudad de Río Grande, Tierra del Fuego.

A partir de información obtenida de publicaciones inmobiliarias reales, se construyó un dataset propio y se evaluaron distintos modelos de regresión con el objetivo de estimar el valor mensual de alquiler de una propiedad en función de sus características.

El trabajo incluye las etapas de:

* Recolección y construcción del dataset.
* Limpieza y preparación de datos.
* Análisis exploratorio de datos (EDA).
* Entrenamiento y evaluación de modelos predictivos.
* Validación cruzada.
* Análisis de residuos.
* Comparación de resultados.
* Discusión de limitaciones y propuestas de mejora.

---

# Dataset

El dataset fue construido manualmente a partir de publicaciones inmobiliarias de:

* Mercado Libre Inmuebles
* Argenprop
* Inmobiliaria Latitud
* Mac Rae Propiedades
* Grupo Inversión

### Características generales

* 167 registros
* 20 variables
* Propiedades ubicadas en Río Grande, Tierra del Fuego
* Información recopilada durante mayo y junio de 2026

Variable objetivo:

**Precio de alquiler (ARS)**

---

# Variables utilizadas en el modelado

* Barrio
* Ciudad
* Ambientes
* Metros²
* Tipo_propiedad
* Amoblado
* Antigüedad
* Baños
* Cochera
* Mascotas_permitidas
* Expensas_incluidas

Variable objetivo:

* Precio

---

# Modelos evaluados

## 1. Regresión Lineal

Resultados:

* MAE: 127.095
* RMSE: 186.998
* R²: 0.757

---

## 2. Árbol de Decisión

Resultados:

* MAE: 75.588
* RMSE: 148.492
* R²: 0.847

---

## 3. Random Forest

Resultados:

* MAE: 74.630
* RMSE: 109.781
* R²: 0.916

Fue el modelo con mejor desempeño general.

---

# Validación Cruzada

Se aplicó validación cruzada de 5 particiones (5-Fold Cross Validation) sobre el modelo Random Forest.

Esta técnica permitió evaluar la capacidad de generalización del modelo sobre distintos subconjuntos de datos, obteniendo una estimación más robusta del desempeño esperado frente a nuevos casos.

---

# Análisis de Residuos

Se realizó un análisis de residuos utilizando las predicciones obtenidas por el modelo Random Forest.

El objetivo fue verificar la distribución de los errores y detectar posibles patrones sistemáticos.

Los resultados muestran una distribución razonablemente aleatoria alrededor de cero, lo que indica que el modelo captura adecuadamente la relación entre las variables predictoras y el precio de alquiler.

---

# Estructura del Repositorio

```text
Aprendizaje_Automatico_Parcial_2026
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── Alquileres_RioGrande.ipynb
    ├── Alquileres_RioGrande_(Entrega 3).ipynb
│   └── Alquileres_RioGrande_(Final).ipynb
│
├── references
│   ├── Programa Aprendizaje Automático 2026.pdf
│   ├── Lineamientos generales.pdf
│   └── Rúbrica de Evaluación.pdf
│
├── reports
│   ├── Informe Técnico.docx
│   ├── Diccionario de Datos.docx
│   └── Presentacion_proyecto.md
│
├── models
│
├── src
│
├── README.md
└── requirements.txt
```

# Limitaciones del Estudio

* Dataset reducido (167 registros).
* Recolección manual de datos.
* Información correspondiente a un período específico del mercado inmobiliario.
* Variables relevantes no disponibles, como estado de conservación, orientación, calidad constructiva o distancia a servicios.

Por estos motivos, los resultados deben interpretarse como una aproximación basada en la información disponible.

---

# Trabajo Futuro

Como líneas de mejora futuras se propone:

* Ampliar el dataset incorporando nuevas publicaciones.
* Incrementar la cobertura temporal del relevamiento.
* Incorporar nuevas variables descriptivas.
* Aplicar optimización de hiperparámetros.
* Evaluar modelos más avanzados como:

  * Gradient Boosting
  * XGBoost
  * LightGBM
* Desarrollar una herramienta interactiva para estimación de precios.

---

# Tecnologías Utilizadas

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* OpenPyXL
* Google Colab
* GitHub

---

# Conclusión

Los resultados obtenidos muestran que es posible estimar precios de alquiler utilizando técnicas de Aprendizaje Automático aplicadas a datos reales del mercado inmobiliario local.

Entre los modelos evaluados, Random Forest presentó el mejor desempeño, alcanzando un coeficiente de determinación R² de 0.916 y los menores errores de predicción, demostrando una elevada capacidad para modelar la variabilidad de los precios de alquiler en Río Grande.


