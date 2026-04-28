## Constenla Nahuel

### Trabajo Aprendizaje Automático

### PRECIOS CORTES DE CARNES

#### Primera Entrega 

Definición del problema será el de abordar el problema de predicción de precios futuros de los productos de la Carne en base al DataSet disponible de una plataforma de Precios a Nivel Provincial.

Este proyecto de Aprendizaje Automático se va a centra en responder a la siguiente pregunta de investigación e Hipótesis:

* ¿Cuáles son los factores más influyentes que determinan los precios de los productos de la Carne en la Ciudad de Río Grande?  
* “¿Es posible predecir con precisión la variabilidad en los Futuros Precios de los Productos de la Carne que la población de Rio Grande consume?”

Factores como el costo de los combustibles que las Empresas de Transportes trasladan al servicio que prestan, el Alimentos para que se provee a los animales, las condiciones climáticas zonales, las políticas Impositivas Nacionales como Provinciales, las tasas al cambio, son algunas de las influencias significativas que afectan a los precios locales de los productos de la carne.
La relevancia de este problema también se acentúa en el contexto de la globalización y el comercio internacional, donde los precios locales pueden verse afectados por eventos en otras partes del país y el mundo, como pandemias, conflictos geopolíticos y cambios en las políticas comerciales.

#### OBJETIVO

El objetivo principal de este proyecto es desarrollar un modelo de Aprendizaje Automático capaz de predecir los precios futuros de productos de la Carne a nivel local. La predicción precisa de estos precios puede proporcionar a las Vecinas y Vecinos de la Ciudad de Río Grande, una ventaja significativa en la toma de decisiones a la hora de planificar una compra Semanal o Mensual. Específicamente, el proyecto se centrará en predecir los precios de diferentes tipos de carnes como Asado, Vacío, tipos de Carne Picada, Etc. utilizando datos históricos y diversas variables que puedan influir en los precios.

#### PROBLEMA A ABORDAR

El problema que este proyecto pretende abordar es la volatilidad y fluctuación de los precios en los Comercios Locales de los productos de la carne en el mercado de la Ciudad de RG. Estos cambios pueden deberse a una variedad de factores, incluyendo cambios en los costos de producción, variaciones estacionales, en la demanda, políticas de impuestos, entre otros. 
La capacidad de prever estas variaciones puede ayudar a mitigar riesgos y optimizar bolsillos de los Vecinos y Vecinas de la Ciudad.

#### SELECCIÓN DEL MODELO

Utilizare un modelo de regresión de Aprendizaje Supervisado, probaremos con un modelo de regresión lineal (LinearRegression), ya que intentaremos predecir valore en este caso precios a futuro de una o más variables.
También desarrollaremos un modelo de Árbol de Decisión (RandomForestRegressor) para mejorar la precisión y la robustez de las predicciones

#### PASOS A SEGUIR

1.- Carga de Librerías necesarias
* Pandas
* Numpy
* Seaborn
* Matplotlib
* sklearn

2.- Exploración de Datos
* Análisis General del DataSet
* Análisis Descriptivo y Estadístico del DataSet
* Análisis de valores nulos y duplicados.

3.- Preprocesamiento
* Conversión de fechas a un formato adecuado 
* Codificación de variables categóricas.
* Normalización o estandarización de precios.

4.- Modelado
* Definición del problema (Predicción de precios futuros, clasificación de productos o análisis de tendencias).
* Selección de algoritmos apropiados (Regresión, Clasificación).
* Entrenamiento y validación del Modelo.

5.- Evaluación
* Métricas de desempeño para evaluar la precisión del modelo.
* Interpretación de resultados y conclusiones.