## Descripción del Dataset y Origen

### Nombre del Dataset: “14_3_03_Produccion_Industrial-1-1.xlsx”

Este dataset es el principal, ya que nos informa la producción mensual de los equipos electrónicos fabricados en Tierra del Fuego. 

Preprocesamiento: Al Dataset original, se reacomodo, filtraro columnas. 

Cantidad de Instancias y Características: Esta compuesto por 147 instancias y 7 atributos. 

Los atribtos son 5 tipo flotantes 2 enteros y uno categorico. 

- Año :               Int

- Mes :               category

- Total  :              Int 

- Aireacondicionado  :  float

- Celulares  :          float

- Microondas  :         float

- Televisor  :          float

- Mod Electr Autom  :   float


Fuente: Instituto Provincial de Análisis e Investigación, Estadística y Censos sobre la base de 
datos de Subsecretaría de Industria del Ministerio de Producción y Ambiente de la Provincia de TDF, AeIAS. 

Fecha de descarga: Mayo-2025
_____________________________________________________________________________________________________


### Nombre del Dataset: "sh_ipcnu.xls", "sh_ipc_2008.xls" y "sh_ipc_05_25.xls"

Estos 3 datasets proveen información relacionada con el índice de inflación. En este proyecto se considera que puede ser una variables que determine el aumneto o disminución de compra de equipos electrónicos por parte de los usuarios. Los tres datasets contienen la misma información pero en períodos diferentes. 

Preprocesamiento: Unificar los 3 datasets de diferentes períodos en uno solo, usando pandas. Creando un nuevo dataset: "Inflacion_mensual-Preprocesada"

Cantidad de Instancias y Características: Esta compuesto por 147 instancias y 4 atributos. 

Los atribtos son 5 tipo flotantes 2 enteros y uno categorico. 

- Año :	        int

- Mes :	        category

- Num_Mes :	    int

- ipc :	float

Fuente: INDEC

Fecha de descarga: Mayo-2025

_____________________________________________________________________________________________________


### Nombre del Dataset: "cotizacion_dolar.xlsx"

La cotización de dolar, puede influir en las empresas en la compra de insumos en el exterior, por lo que se consideró agregar este dataset. 
Preprocesamiento: El dataset de descarga de una pagina web, con la función "pd.read_html(url)". Se pasan las filas a columnas. Se agrega columna mes con su equivalente ordinal. 

Cantidad de Instancias y Características: Esta compuesto por 150 instancias y 4 atributos. 

Los atribtos son 5 tipo flotantes 2 enteros y uno categorico. 

- Año :	        int

- Mes :	        category

- Num_Mes :	    int

- Cotizacion :	float


Fuente: https://estudiodelamo.com/cotizacion-historica-dolar-peso-argentina/

Fecha de descarga: Mayo-2025
_____________________________________________________________________________________________________


### Nombre del Dataset: "WorldCupMatches.csv"

Este dataset se incorpora al análisis, para el modelado de producción de televisores. Es sabido que un disparador en la fabricación de tv en nuestro país esta relacionado con este evento. 

Preprocesamiento: El dataset de descarga de una pagina web, con la función "pd.read_html(url)". Se pasan las filas a columnas. Se agrega columna mes con su equivalente ordinal. Se toma como valor si se se desarrollo o no el mundial en cada mes. 

Cantidad de Instancias y Características: Esta compuesto por 150 instancias y 4 atributos. 

Los atribtos son 5 tipo flotantes 2 enteros y uno categorico. 

- Año :	        int

- Mes :	        int

- Mundial :	    int
 


Fuente: [https://www.goal.com/es-ar/noticias/todas-las-finales-de-los-mundiales/8k21jcs1v7321xkkfde58ectl]
Fecha de descarga: Junio-2025
_____________________________________________________________________________________________________
