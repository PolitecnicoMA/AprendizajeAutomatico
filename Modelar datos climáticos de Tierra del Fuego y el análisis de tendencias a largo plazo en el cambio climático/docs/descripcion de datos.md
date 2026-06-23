![Texto alternativo](dataset.jpg)

DESCRIPCION DEL CONJUNTO DE DATOS

Origen del Dataset
•  Instituto Provincial de Análisis e Investigación, Estadística y Censos sobre los datos de Base Aeronaval Río Grande y del Centro Austral de Investigaciones Científicas..

• Fuente: Servicio Meteorológico Nacional.

• Fecha de Adquisición: 11 de Octubre de 2024.

• Recopilación: Los datos fueron descargados de la pagina del IPIEC.

• Política de Datos: Comprendidos dentro de la Política de Datos Públicos, por lo que son gratuitos.

• Nota: La información básica en el archivo puede sufrir variaciones debido a procesos de consistencia y depuración.

Descripción del Dataset
• Cantidad de Instancias: El dataset contiene datos Mensuales y anuales de la estación meteorológica Rio Grande y del Centro Austral de Investigaciones Científicas. desde el 1 de enero de 2009 hasta el 31 de diciembre de 2022.

• Periodo Cubierto: 14 años completos.

• Frecuencia: mensual y anual.

• Total de Instancias: 168 registros mensuales y 14 registros anuales.

Características (Columnas) y Tipos de Datos

Período: Representa el intervalo de tiempo durante el cual se registraron los datos (Meses: categorico Años: Entero) 

Temperaturas:

Máxima Media: Promedio de las temperaturas máximas durante el período.(float)

Mínima Media: Promedio de las temperaturas mínimas durante el período.(float)

Media: Promedio general de las temperaturas durante el período.(float)

Precipitaciones:

Lluvia Caída: Cantidad total de lluvia registrada en el período.(float)

Días con Nieve: Número de días en los que se registró nieve durante el período.(entero)

Variable 1:	Temperatura media 

Definición Operativa: La temperatura atmosférica refiere al grado de calor específico presente en el aire en un lugar y momento determinados. 

La temperatura media mensual hace referencia al promedio de las temperaturas medias diarias (promedio de la máxima y mínima diaria).

Unidad de Medida:	°C Grado Celsius

Método de Cálculo (formula):	T°media: (T°M + T°m)/2


Variable 2:	Temperatura máxima media mensual

Definición Operativa: 	La temperatura máxima media mensual resulta del promedio de las temperaturas máximas absolutas que se registran en forma diaria durante el mes.

Unidad de Medida:	°C Grado Celsius

Método de Cálculo (formula):	T°Mme: ∑ T°M/nT°M


Variable 3:	Temperatura mínima media mensual

Definición Operativa: 	La temperatura mínima media mensual resulta del promedio de las temperaturas mínimas absolutas que se registran en forma diaria durante el mes.

Unidad de Medida:	°C Grado Celsius

Método de Cálculo (formula):	T°mme: ∑ T°m/nT°m


Variable 4:	Precipitaciones (mm)

Definición Operativa: 	Corresponde a cualquier producto de la condensación del vapor de agua atmosférico que se deposita en la superficie de la Tierra. 

Unidad de Medida:	Milímetros (mm)  altura de la lámina de agua recogida de una superficie plana. 

Método de Cálculo (formula):	Sumatoria de milimetros de agua líquida caída en forma de gotas por mes. 1mm= 1 litro/m2, captados durante un lapso de 24hs. 


Variable 5	Días con nieve

Definición Operativa:	Cantidad de dias del mes en los que se han registrado nevadas.

Unidad de Medida:	Día

Método de Cálculo (formula):	Sumatoria de días al mes que han registrado precipitaciones


• Valores Faltantes: Existen valores faltantes o nulos en algunas columnas, especialmente en las relacionadas con los dias con presencia de nieve.

Procesos de Preprocesamiento
Para preparar este dataset para un proyecto de aprendizaje automático, se podrían considerar los siguientes pasos de preprocesamiento:

Manejo de Valores Faltantes: Imputar o eliminar registros con valores nulos.

Conversión de Tipos de Datos: Asegurar que todos los datos están en el formato correcto.

Normalización/Estandarización: Dependiendo del algoritmo a utilizar, podría ser necesario normalizar o estandarizar los datos.

Generación de Nuevas Características: Crear características adicionales como promedios móviles o variaciones diarias.