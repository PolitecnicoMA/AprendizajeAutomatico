# Contexto
La Provincia de Tierra del Fuego es una de las principales regiones productoras de hidrocarburos en Argentina. Los ingresos provenientes de las regalías petroleras (pagos realizados por las empresas que explotan el recurso) constituyen una fuente crítica para el financiamiento del presupuesto provincial. Estas regalías están directamente relacionadas con factores como el volumen de producción, el tipo de crudo y el precio de venta, los cuales presentan variaciones mensuales.

En este contexto, contar con herramientas que permitan anticipar el comportamiento futuro de las regalías resulta fundamental para la gestión pública y la planificación financiera de la provincia. Si bien existen métodos tradicionales para realizar estimaciones económicas, este proyecto propone abordar el problema desde un enfoque basado en Aprendizaje Automático.

# Objetivo del Proyecto
El objetivo del proyecto es predecir el monto mensual de regalías petroleras que recibirá la Provincia de Tierra del Fuego, utilizando técnicas de Aprendizaje Supervisado y tomando como base datos históricos provenientes del portal oficial del Ministerio de Economía (datos.energia.gob.ar). La intención es capturar patrones que relacionan producción, tipo de crudo y precios con los ingresos por regalías, para después proyectar posibles escenarios futuros.

## Objetivo General
Desarrollar un modelo de Aprendizaje Automático capaz de predecir el monto mensual de regalías petroleras recibidas por la Provincia de Tierra del Fuego, utilizando datos históricos de producción, tipo de crudo y precios.

## Objetivos Específicos
- Filtrar y preparar un dataset con registros mensuales exclusivamente de Tierra del Fuego.
- Analizar las variables que afectan directamente el monto de regalías (producción, tipo de crudo, precio).
- Aplicar modelos de regresión supervisada para predecir valores continuos de ingresos mensuales.
- Evaluar el desempeño de los modelos mediante métricas apropiadas (MAE, MSE, R²).
- Interpretar los resultados obtenidos para su posible uso en la planificación presupuestaria.

## Tipo de Problema
Se trata de un problema de regresión supervisada, ya que el objetivo es predecir el monto mensual de regalías petrolera, que es una variable numérica continua.

## Modelos Posibles a Utilizar
Para abordar el problema, se consideran los siguientes modelos de regresión incluidos en la librería scikit-learn:
- Regresión Lineal.
- Ridge Regression.

Durante el desarrollo del proyecto, voy a evaluar el rendimiento de cada uno de estos modelos para determinar cuál se adapta mejor al problema planteado.

## Fuente de Datos
El dataset fue extraído del portal de datos abiertos del Ministerio de Economía: http://datos.energia.gob.ar
Archivo seleccionado: “Informe Regalias CRUDO.xlsx”
Éste archivo contiene información mensual por provincia sobre:
- Fecha (AÑO / MES)
- Provincia
- Precio (por m³)
- Producción (m³)
- Monto total de regalías
- Tipo de crudo

## Documentación Complementaria
- Cierre Estadístico 2021 TdF: 
https://www.argentina.gob.ar/sites/default/files/informe_productivo_tierra_del_fuego_web_2022.11.pdf
- Regalías Decreto N° 1.671/1969: 
https://servicios.infoleg.gob.ar/infolegInternet/anexos/225000-229999/228310/norma.htm
- Decreto Prov. N° 1292/17: 
https://www1.tcptdf.gob.ar/wp-content/uploads/decretos/Decreto-Provincial-N-1292-2017.pdf

# Enlace de Google Colab
https://colab.research.google.com/drive/141ELtuKipYpEhBI4YwGWT3W7wSna-sKT?usp=sharing

# Enlace de Video Youtube
https://youtu.be/L9dsltRYvi0

# Enlace de Video Google Drive
https://drive.google.com/file/d/1NfhHVHXPbVQrABn9zRw4-Cjf6xqh0Cjd/view?usp=sharing
