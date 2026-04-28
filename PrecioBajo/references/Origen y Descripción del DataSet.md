## Origen y Descripción del DataSet "Carnes.csv

**Los Datos son provenientes de la Platafoma "https://preciobajo.com.ar"**

------------

Se solicito por Correo Electronico a la platafoma un Set de Datos que contenga, el comercio, que productos es y el precio segun el dia que se relevo, de todos los cortes de Carnes que la plataforma informa a la vecina y Vecino. Se recibio un archivo con formato .xlsx el cual se analizo cargandolo desde el Jupyter del Trabajo mostrando lo Siguiente:

**El Dataset tiene:**

*Cantidad de instancias: 6559 registros (filas).
*Características (columnas): 5
    *proveedor: Nombre del proveedor - tipo de dato object-(cadena de texto).
    *categoria: Nombre del Categoria del Producto - tipo de dato object-(cadena de texto).
    *producto: Tipo de producto de carne - tipo de dato object-(cadena de texto).
    *fecha: Fecha del registro - tipo de dato object-(cadena de texto).
    *precio: Precio del producto - tipo de dato int64-(entero).

------------

#### Diccionario de datos

| Variable | Descripción | Tipo de Dato |
| ------------ | ------------ | ------------ |
| Proveedor | Nombre del Comercio en el cual se releva el precio del producto. | Cadena de Caracteres. |
| Categoria | Nombre de la Categoria que le corresponde al producto. | Cadena de Caracteres. |
| Producto | Nombre del Producto de la Carne que se releva el Precio. | Cadena de Caracteres. |
| Fecha | Fecha del Dia y Hora del registro de escaneo del precio del producto | Cadena de Caracteres. |
| Precio| Valor que corresponde a 1 Kg. (1000 g.) de Producto relevado. | Numero entero. |


*El archivo fue recibido el dia Lunes 11 de junio y solicitados con anterioridad, los datos correponden a una fecha que va desde 01 de Marzo hasta el dia 11 de Junio.*

------------

#### Luego de Analisis  del DataSet - Pasos a seguir:

1.- Exploración de Datos:
    * Resumen estadístico del dataset.
    * Análisis de valores nulos y duplicados.

2.- Preprocesamiento:
    * Conversión de fechas a un formato adecuado y extracción de características temporales.
    * Codificación de variables categóricas.
    * Normalización o estandarización de precios.

**El Resumen Estadístico y nos muestra que:** 

- Hay 6558 registros en total.
- Hay 15 proveedores y 39 productos únicos.
- La columna de fecha tiene 1097 valores únicos.
- El precio promedio es de aproximadamente 7959.07, con una desviación estándar de 2091.37.
- Los precios varían desde 1490 hasta 17730.

**Realizamos una Descipcion Basica de las distintas variables del DataSet**

* Cantidad: 6559
* Media: 7959.07
* Devio Standard: 2091.37 
* Valor Minimo: 1490
* Primer Cuartil: 6500
* Segundo Cuartil: 7990
* Tercer Cuartil: 8999
* Valor Maximo: 17730

**No hay valores nulos, pero se encontró un registro duplicado.**

El Trabajo sobre el DataSet Corresponde al Archico "Examen_Parcial_V1"

notebooks/Examen_Parcial_V1.ipynb