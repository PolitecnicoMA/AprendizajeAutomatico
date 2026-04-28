## Reporte de Resultados - Trabajo Aprendizaje Automático

### PRECIOS CORTES DE CARNES

#### Librerias utilizadas
* Pandas
* numpy
* seaborn
* matplotlib
* sklearn

#### Exploración de Datos
* Se realizo un análisis exploratorio de los datos para entender mejor su estructura y contenido, (Archivo Carnes.csv). 
* El DataSet tiene 6558 registros y Cinco (5) Columnas: 1.Proveedor, 2.Categoria, 3.Producto, 4.Fecha y 5.Precio. 

#### El Analisis Descriptivo demuestra que:
* Cantidad: 6559
* Media: 7959.07
* Devio Standard: 2091.37
* Valor Minimo: 1490
* Primer Cuartil: 6500
* Segundo Cuartil: 7990
* Tercer Cuartil: 8999
* Valor Maximo: 17730

#### El Resumen Estadístico nos muestra que:
* Hay 6559 registros en total.
* Hay 15 proveedores y 38 productos únicos.
* La columna de fecha tiene 1097 valores únicos.
* El precio promedio es de aproximadamente 7959.07, con una desviación estándar de 2091.37.
* Los precios varían desde 1490 hasta 17730.

#### Preprocesamiento de Datos
* Eliminación de duplicados: Eliminaremos los registros duplicados.
* Conversión de la columna de Fecha: Convertiremos la columna de Fecha al tipo datetime y quedara solo año/mes/día.

**Al DataSet se han eliminando registros duplicados y se convirtio fecha en el tipo de dato necesario.**

### Visualización de Datos

* Boxplot que Visualizar los Precios por Proveedor (\PrecioBajo\reports\figures\Imagen_1.png)
* Análisis del gráfico 
    El gráfico "Precios por Proveedor" muestra los precios de los Productos ofrecidos por los diferentes Proveedores, el eje horizontal del gráfico muestra los Proveedores, mientras que el eje vertical muestra los Precios.
    Los precios de los productos son relativamente estables entre los diferentes proveedores, sin embargo, hay algunas variaciones en los precios, especialmente para algunos productos específicos.
    Por ejemplo, el precio del producto "Alta Performance" varía desde 10000 hasta 18000, mientras que el precio del producto "La vaca austral varía desde 6000 hasta 8000.

**Filtro los Datos de un proveedor específico** 

* Boxplot de Precios de los Productos por un Proveedor especifico (\PrecioBajo\reports\figures\Imagen_2.png)
    El gráfico muestra los precios de 23 productos de cortes de Carnes de un mismo proveedor.
    Los precios varían considerablemente, desde un mínimo 4000 para la carne picada especial hasta un máximo de 10000 para el Asado. Productos más caros son el asado, el bife ancho, el bife angosto y los Productos más baratos son la carne picada especial, la falda c/hueso, por nombrar Productos.
    Ejemplos:
    * El precio del asado ha aumentado significativamente en los últimos meses, el precio actual es de 10000 por kg, lo que lo convierte en el producto más caro del gráfico.
    * El precio de la carne picada especial ha sido relativamente estable en estos meses, el precio actual es de 4000 por kg, lo que lo convierte en el producto más barato del gráfico.

* Histograma de precios de todos los productos (\PrecioBajo\reports\figures\Imagen_3.png)
    Análisis de la distribución de los Precios, la distribución es asimétrica a la derecha ya que la mayoría de los precios se encuentran en el extremo inferior del rango de precios, y hay una menor cantidad de precios en el extremo superior.

**Filtramos datos de un producto específico para la serie temporal (ejemplo: 'Asado x Kg.')**

* Grafico para la serie temporal del Producto (\PrecioBajo\reports\figures\Imagen_4.png)
    El gráfico muestra una tendencia decreciente del Precio del Asado por Kg. durante el período que se analiza, el precio comienza en 9250 el 1/5/24 y termina en 7750 el 8/6/24 lo que representa una disminución representa una caída del 16,5 %.
    La mayor caída se produce entre el 1/5 y el 8/5, cuando el precio baja de 9250 a 8750, una disminución del 5,3 %. 
    A partir de ahi, el precio se modera, con una disminución del 2,4 % entre el 8/5 y el 15/5, del 0,7 % y asi hasta caer un 1,3 % entre el 22/5 y el 8/6.

* Grafico de Dispersion de los Precios de todos sus productos (\PrecioBajo\reports\figures\Imagen_5.png)
    Los puntos de datos están dispersos por todo el gráfico, lo que indica que no hay una relación lineal perfecta y no se observan valores atípicos en el gráfico.

* Histograma que muetra cantidad de productos en cada rango de precios (\PrecioBajo\reports\figures\Imagen_6.png)
    El Histograma indica que la mayor cantidad de cortes de carnes se venden en un rango de precios relativamente estrecho, alrededor de 9000 a 1000.

#### Modelado y Evaluación de los Datos
* Codificación de las variables categóricas "PROVEEDOR y PRODUCTO"
* Selección de características (X) y variable objetivo (y)
    X para "PROVEEDOR y PRODUCTO"
    Y para "PRECIO"
* División de los datos en entrenamiento y prueba 70 / 30

#### METODO DE REGRESIÓN LINEAL

**RESULTADO**

**DATOS DE ENTRENAMIENTO**
* Error absoluto medio = 1712.984
* Error cuadratico medio = 4888211.91
* Puntuación R2 = 0.033
* Error absoluto mediano = 1400.957
* Puntuación de varianza explicada = 0.033
 
 **DATOS DE PRUEBA**
* Error absoluto medio = 1273.743
* Error cuadratico medio = 2914446.95
* Puntuación R2 = -0.066
* Error absoluto mediano = 933.537
* Puntuación de varianza explicada = -0.066

* Grafico del Modelo de Regresión "LinearRegression# (\PrecioBajo\reports\figures\RegresionLineal.png)

#### Informe del Modelo

**Descripción del Resultado del Método**
    Se utilizó un modelo de regresión lineal para predecir el precio de los productos de carne basándose en dos características, "Proveedor y Producto#. Los datos fueron divididos en un conjunto de entrenamiento (70%) y un conjunto de prueba (30%).
    El valor de R² (0.033) indica que el modelo no se ajusta bien a los datos, ya que está cerca de 0 para el conjunto de entrenamiento y es negativo (-0.066) para el conjunto de prueba, lo que sugiere que el modelo tiene un rendimiento deficiente en la predicción de los precios.

**Gráfico**
    El gráfico muestra una comparación entre los valores reales de los precios (eje X) y las predicciones realizadas por el modelo (eje Y) para el conjunto de prueba. 
    Cada punto azul representa un precio real y su correspondiente predicción y la línea roja representa una predicción perfecta (donde el valor real es igual al valor predicho)

#### METODO DE ARBOL

**RESULTADO**

 **DATOS DE ENTRENAMIENTO**
* Error absoluto medio = 315.1098877915395
* Error cuadratico medio = 394529.8967742431
* Puntuación R2 = 0.9169035118388641
* Error error absoluto mediano = 129.5999999999999
* Varianza = 0.917157973130365

* Grafico del Modelo de Regresión "LinearRegression# (\PrecioBajo\reports\figures\ArbolD2.png)

#### Informe del Modelo

**Descripción del Resultado del Método**
El modelo de Árbol de Decisión fue entrenado con el 70% de los datos y evaluado con el 30% restante, el resultado indica que el modelo tiene una buena capacidad predictiva, con una alta varianza explicada y un error relativamente bajo.

**Gráfico**
El gráfico muestra la comparación entre los valores reales y los valores predichos por el modelo, el Eje X representa los valores reales de los precios y el eje Y representa los valores predecidos de los precios.
La mayoría de los puntos están cercanos a la línea de referencia, lo que indica que las predicciones del modelo están bastante alineadas con los valores reales. 
Esto refuerza las métricas de evaluación que muestran un buen desempeño del modelo, con un alto valor de R² y errores absolutos relativamente bajos.