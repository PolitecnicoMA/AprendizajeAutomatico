### PROYECTO EVALUATIVO DE APRENDIZAJE AUTOMATICOS

###Segmentación mediante detección de patrones en población adulta en el consumo de psicofármacos con fines terapéuticos

## Analisis Exploratorio

##Descripción del dataset final

Para el desarrollo del presente proyecto se construyó un dataset integrado orientado al análisis de patrones de consumo de psicofármacos con fines terapéuticos en población adulta. El objetivo de esta base de datos es servir como insumo para la aplicación de técnicas de Aprendizaje Automático no supervisado, específicamente métodos de segmentación o clustering que permitan identificar perfiles de consumo similares entre los individuos.
El dataset final fue generado a partir de la integración de tres bases de datos públicas pertenecientes a la encuesta Medical Expenditure Panel Survey (MEPS). Cada registro del dataset representa a una persona encuestada y reúne información demográfica, socioeconómica, sanitaria y farmacológica.
La unidad de análisis del dataset corresponde a individuos adultos participantes de la encuesta.
Cantidad de instancias

El dataset final contiene aproximadamente 27.805 instancias, donde cada fila representa una persona identificada mediante la variable DUPERSID.

## Cantidad de variables
La base final está compuesta por variables provenientes de los tres archivos originales y por variables derivadas construidas durante el proceso de preprocesamiento. Las variables seleccionadas fueron aquellas consideradas relevantes para el análisis del consumo de psicofármacos y la posterior aplicación de algoritmos de clustering.

## Diccionario de variables del dataset final


| Variable | Descripción | Tipo de dato | Clasificación |
|----------|-------------|--------------|----------------|
| DUPERSID | Identificador único de cada individuo | Entero/String | Cualitativa nominal |
| AGE20X | Edad del individuo | Entero | Cuantitativa discreta |
| SEX | Sexo del individuo | Categórica | Cualitativa nominal |
| MARRY20X | Estado civil | Categórica | Cualitativa nominal |
| EDUCYR | Años de educación completados | Entero | Cuantitativa discreta |
| POVCAT20 | Categoría de ingresos según nivel de pobreza | Categórica | Cualitativa ordinal |
| EMPST53 | Situación laboral | Categórica | Cualitativa nominal |
| INSCOV20 | Cobertura médica | Categórica | Cualitativa nominal |
| MNHLTH53 | Estado de salud mental autopercibido | Categórica | Cualitativa ordinal |
| RTHLTH53 | Estado general de salud autopercibido | Categórica | Cualitativa ordinal |
| RACETHX | Grupo racial o étnico | Categórica | Cualitativa nominal |
| cantidad_condiciones | Cantidad de condiciones médicas registradas | Entero | Cuantitativa discreta |
| recetas_totales | Cantidad total de medicamentos prescritos | Entero | Cuantitativa discreta |
| benzodiacepinas | Cantidad de benzodiacepinas consumidas | Entero | Cuantitativa discreta |
| antidepresivos | Cantidad de antidepresivos consumidos | Entero | Cuantitativa discreta |
| hipnoticos | Cantidad de hipnóticos consumidos | Entero | Cuantitativa discreta |
| ansioliticos | Cantidad de ansiolíticos consumidos | Entero | Cuantitativa discreta |
| total_psicofarmacos | Total de psicofármacos consumidos | Entero | Cuantitativa discreta |

## Información relevante del dataset

El dataset integra información proveniente de distintas dimensiones relacionadas con la salud y el consumo de medicamentos:
•	Características demográficas. 

•	Características socioeconómicas. 

•	Estado de salud general. 

•	Estado de salud mental. 

•	Condiciones médicas diagnosticadas. 

•	Medicamentos prescritos. 

•	Consumo específico de psicofármacos. 

La combinación de estas dimensiones permite analizar posibles relaciones entre variables sociales, económicas y sanitarias con los patrones de consumo de medicamentos utilizados para el tratamiento de trastornos de ansiedad, depresión y alteraciones del sueño.


## Origen de los datos
Los datos utilizados en este proyecto provienen de la encuesta pública Medical Expenditure Panel Survey (MEPS), desarrollada por la Agency for Healthcare Research and Quality (AHRQ), organismo dependiente del Departamento de Salud y Servicios Humanos de los Estados Unidos.
MEPS es una de las principales fuentes de información sobre salud pública, utilización de servicios sanitarios, cobertura médica, gastos en salud y consumo de medicamentos. Los datos son de acceso público y se encuentran disponibles para investigación académica y científica.
Los archivos utilizados fueron descargados desde el portal oficial de MEPS durante el desarrollo del proyecto y posteriormente procesados mediante Python utilizando la biblioteca Pandas.

## Descripción de los datasets originales (3)
Luego de una ardua y extensa navegacion por diferentes sitios de busqueda de datos, de la consulta con numerosas inteligencias artificiales, mi criterio fue la eleccion de estos tres set de datos , que para mi se inclinan mejor con lo que quiero trabajar y que tienen que ver con el objetivo principal. Se desestimaron numerosos set de datos y se trabajó con el apoyo de la inteligencia artificial en momentos donde el codigo se complicaba. 
Para la construcción del dataset final se utilizaron tres archivos pertenecientes a MEPS.

1)	Dataset H224 – Full-Year Consolidated Data File
Este archivo contiene información consolidada de las personas encuestadas durante el período de estudio.

## Características principales

•	27.805 registros. 

•	1.451 variables. 

## Información incluida

•	Edad. 

•	Sexo. 

•	Estado civil. 

•	Nivel educativo. 

•	Situación laboral. 

•	Ingresos. 

•	Cobertura médica. 

•	Estado de salud general. 

•	Estado de salud mental. 

•	Características demográficas. 

Este archivo constituye la base principal sobre la cual se realizó la integración de los demás datasets.

## 2)	Dataset H222 – Medical Conditions File
Este archivo registra las condiciones médicas reportadas por los individuos encuestados.

## Características principales

•	80.802 registros. 

•	30 variables. 

Información incluida

•	Diagnósticos médicos. 

•	Códigos de clasificación de enfermedades. 

•	Condiciones de salud reportadas. 

•	Vinculación entre individuos y diagnósticos. 

Este dataset permitió construir variables relacionadas con la cantidad de condiciones médicas asociadas a cada individuo.

## 3)	Dataset H229A – Prescribed Medicines File
Este archivo contiene información sobre medicamentos prescritos a los participantes de la encuesta.

## Características principales

•	303.394 registros. 

•	66 variables. 

Información incluida

•	Nombre comercial del medicamento. 

•	Nombre genérico. 

•	Clasificación terapéutica. 

•	Cantidad de recetas. 

•	Información farmacológica. 

Este dataset permitió identificar y clasificar medicamentos pertenecientes a las categorías de interés para el proyecto.

Proceso de integración y construcción del dataset final. (Este proceso tambien queda registrado en el jupyter notebook y va a estar incluido en los archivos en el Git “unificacion_psicofarmacos_fina.ipynb”).
La construcción del dataset final requirió una serie de tareas de preparación y preprocesamiento de datos.

Importación de los archivos
Se importaron los archivos H224, H222 y H229A utilizando la biblioteca Pandas en Python.


## Exploración inicial

Se analizaron las dimensiones de cada dataset, los tipos de datos presentes y la calidad de la información disponible.
Selección de variables
Debido a la gran cantidad de variables presentes en los archivos originales, se seleccionaron aquellas consideradas relevantes para el estudio del consumo de psicofármacos y la caracterización de la población adulta.
identificación de la clave de integración
Los tres datasets comparten la variable DUPERSID, identificador único asignado a cada individuo dentro de la encuesta. Esta variable fue utilizada para relacionar la información contenida en los distintos archivos.

## Construcción de variables farmacológicas
A partir del archivo H229A se identificaron medicamentos pertenecientes a las siguientes categorías:

•	Benzodiacepinas. 

•	Antidepresivos. 

•	Hipnóticos. 

•	Ansiolíticos. 

## Posteriormente se calcularon indicadores agregados por individuo, tales como:

•	Cantidad total de recetas. 

•	Cantidad de benzodiacepinas consumidas.

•	Cantidad de antidepresivos consumidos. 

•	Cantidad de hipnóticos consumidos. 

•	Cantidad de ansiolíticos consumidos. 

•	Total de psicofármacos consumidos. 

## Construcción de variables sanitarias
A partir del archivo H222 se calcularon indicadores relacionados con la cantidad de condiciones médicas registradas para cada individuo.
Integración de datasets

Los tres archivos fueron integrados mediante operaciones de unión utilizando la variable DUPERSID como clave principal.
Tratamiento de valores faltantes
Los registros sin información en determinadas variables derivadas fueron tratados mediante reemplazo por valores nulos o cero según correspondiera.
Generación del dataset final: “dataset_psicofarmacos_final.csv”

Finalmente se obtuvo un dataset consolidado que integra información demográfica, socioeconómica, médica y farmacológica, el cual será utilizado en la tercera etapa del proyecto para la aplicación de técnicas de aprendizaje automático.

