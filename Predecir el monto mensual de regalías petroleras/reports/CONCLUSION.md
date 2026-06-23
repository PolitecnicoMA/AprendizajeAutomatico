En el presente proyecto desarrolle un modelo de Aprendizaje Supervisado con el objetivo de predecir el monto mensual de regalías petroleras que recibe la Provincia de Tierra del Fuego. Para lo que integre datos históricos del Ministerio de Economía, enfocados en tres variables claves, volumen de producción, precio del crudo y monto total de regalías.

A partir de un proceso de limpieza, normalización y combinación de datos provenientes de distintas hojas del archivo original, construi un dataset consolidado con 420 registros mensuales válidos. El análisis exploratorio mostró una fuerte correlación entre producción y regalías, mientras que la relación con el precio resultó más dispersa.

Entrené dos modelos, uno de regresión lineal y otro de regresión Ridge. En el primero obtuve un R² de 0.616 con un error cuadrático medio (RMSE) de 441.831 ARS, mientras que el modelo Ridge mejoró levemente los resultados con un R² de 0.619 y un RMSE de 439.852 ARS. Esto demuestra que, si bien la regularización aplicada no modificó sustancialmente el rendimiento, sí logró una leve mejora en la capacidad predictiva.

Durante el desarrollo del proyecto detecté también ciertos valores atípicos y casos particulares (como predicciones negativas, precios iguales a cero o meses con regalías inesperadamente bajas a pesar de una producción elevada) que surgieron claramente al analizar los gráficos de dispersión. Estas visualizaciones me permitieron no solo entender cómo se comportaban las variables, sino también identificar anomalías que no eran tan evidentes en las tablas.

El modelo desarrollado permite identificar tendencias generales en los ingresos provinciales y podría servir de base para futuras estimaciones económicas más precisas, especialmente en contextos de planificación pública y presupuestaria. Esta necesidad de previsibilidad cobra aún mayor relevancia considerando que el régimen de regalías hidrocarburíferas se encuentra regulado por normativa nacional (Ley 17.319 y Decreto 1277/2012), que establece que las provincias productoras perciben un porcentaje fijo sobre el valor del petróleo extraído.

En el caso particular de Tierra del Fuego, tal como se detalla en el Informe Productivo Provincial (2022), los ingresos por regalías representan una fuente crítica de financiamiento, en una economía donde el sector hidrocarburífero sigue teniendo un peso estratégico. En este sentido, aplicar modelos de Aprendizaje Automático que anticipen posibles escenarios de ingreso no solo es técnicamente viable, sino también funcional a la gestión económica de la provincia. Herramientas como estas podrían integrarse a mediano plazo a sistemas de proyección fiscal o de evaluación de políticas energéticas provinciales



