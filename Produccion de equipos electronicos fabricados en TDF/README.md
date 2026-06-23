# Proyecto: Produccion de equipos electronicos fabricados en TDF
 Alumna: Velasquez Marisa
 
   ![LOGO TDF](https://github.com/user-attachments/assets/7ba3cbcb-a8f0-488d-952f-ad966a5227da)

## Descripción:

El proyecto se centra en la optimización de la producción de cinco productos
electrónicos fabricados en las industrias de tierra del Fuego. Entre ellos Televisor,
Aire acondicionado, Horno microondas, celulares y autoradio.


## Contexto del problema en relación con la provincia

El contexto económico y los desafíos específicos de la provincia de Tierra del Fuego
hacen que este proyecto de machine learning sea relevante y necesario. Al abordar
la producción en las fábricas locales, se busca no solo mejorar la eficiencia y
competitividad, sino también contribuir al desarrollo económico y sustentable de la
región.
Decidí enfocarme en este ámbito por su importancia, ya que lo considero un pilar
clave en la economía de Tierra del Fuego. Desarrollar un modelo de regresión
sobre su funcionamiento puede revelarnos oportunidades para aumentar la
competitividad y la productividad de las industrias locales. Además, una
comprensión más profunda de estos aspectos puede contribuir a la creación de
políticas más informadas y a una gestión más eficaz de los recursos disponibles.


## Objetivo del modelo

El objetivo principal y específico del proyecto es predecir la producción futura de
cada producto electrónico utilizando datos históricos como base para el análisis.
Esta capacidad de anticipación brindará a las fábricas una ventaja competitiva
significativa, ya que les permitirá no solo preveer la demanda de sus productos,
sino también optimizar el uso de los recursos disponibles.

## Preguntas de investigación:

Las preguntas que se prentende responder son: ¿Cuáles son las
tendencias de producción para cada producto? ¿Existen patrones estacionales en la
producción de los productos?

## Modelado

El dataset original con el que cuento sólo me brinda la información de la
producción mensual de cada producto, por lo que la regresión lineal simple era mi
primera opción. Sin embargo, he decidido agregar 2 dataset más. El primero con la
información de tipo de cambio del dólar lo cual entiendo influye en la decisión de
la inversión de las empresas. Y el segundo con el valor de la inflación mensual. Esto
agregará más variables para generar un modelo más acorde. Por lo que para el
modelado estimo que utilizare el de regresión lineal múltiple.
Esta capacidad de anticipación brindará a las fábricas una ventaja competitiva
significativa, ya que les permitirá no solo preveer la demanda de sus productos,
sino también optimizar el uso de los recursos disponibles.

## Estructura del proyecto


                   
```
├── data/                                
│   ├── raw/                  # Datos originales sin procesar
│   ├── processed/            # Datos listos para entrenar
│   └── interim/              # Datos intermedios
│
├── docs/                     # Documentación del proyecto
│   └── dataset_description.md
│
├── models/                   # Modelos entrenados y serializados
│
├── notebooks/                # Jupyter notebooks para análisis exploratorio, entrenamiento y pruebas
│    
│
├── references/               # Artículos, papers, papers técnicos o benchmarks
│
├── reports/                  # Reporte final generado
│   ├── figures/              # Gráficos 
│   └── Análisis de Resultados          # Reportes de evaluación del modelo
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

```
## Enlace al Video Explicativo: 
https://drive.google.com/file/d/11ZukycR2jUe4dfATPr88C4bJDQ9DouYw/view?usp=sharing





Fin...
