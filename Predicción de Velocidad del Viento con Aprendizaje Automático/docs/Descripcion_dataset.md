Presentación completa del dataset
Descripción Completa del Dataset 
Este dataset final, que se va a utilizar para el modelado se a construido con los datos brutos de la página de la estación astronomía de Rio Grande.
•	Nombre del Dataset Procesado: 04-2025.csv
•	Cantidad de filas 945 días de registro de datos de velocidad del viento. Este numero sale de la cantidad de registros que se saco de la pagina mencionada antes, algunos registros tienen datos nulos o faltante.
•	Cantidad Columnas: 22 columnas en total. 
•	Tipos de Datos Principales: 
o	AMD (Fecha): datetime64[ns] (para la fecha del registro).
o	vientomediokm/h: float64 (la variable objetivo a predecir).
•	Rango de Fechas Cubierto: Los datos abarcan desde Noviembre de 2022 hasta Abril de 2025. La serie es de registros diarios.
•	Información adicional: Al dataset lo enfoco en la velocidad del viento, pero incluye otras variables meteorológicas relevantes como temperaturas (media, máxima, mínima, hora de registro de esa máxima y mínima), ráfagas, dirección, presión, lluvia y radiación.

Informe sobre el origen del dataset
Este data set es la página http://earg.fcaglp.unlp.edu.ar/meteorologia/boletin/, lo cual para tomar los datos lo tuve que hacer de forma manual, ya que ellos cobran a las personas que quieran usar los datos.
Adjunto foto(al ser un txt no puedo adjuntar la foto lo tengo igual en un Word)
por cada informe meteorológico que es mensual se cobra un monto de $25000 pesos, lo cual costa de la información presetaba en el boliten meteorologico publicado en la estación astronómica de rio grande
 
Quise empezar a tomar los datos haciendo El scraping, pero se me complico bastante a la hora de tomar los datos de filas y columnas( me traía cualquier cosa) para no perder tiempo averigüe para pedir el dataset y ser costoso no tuve otra opción que sacarlo de forma manual.
Este data set se obtuvo de un dominio publico y todavía no esta manipulado.
