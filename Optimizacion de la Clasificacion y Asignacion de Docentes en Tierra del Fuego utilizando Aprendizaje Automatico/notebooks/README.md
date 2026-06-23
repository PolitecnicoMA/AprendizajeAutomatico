# Notebooks
## La carpeta está organizado en los siguientes archivos:

- **1-Descripción del dataset.ipynb`**
- **2-Limpieza y Tratamiento de Datos .ipynb**
- **3-Modelo_Regresion_Logistica.ipynb**
- **4-Arbol_Decision.ipynb**
- **5-Modelo_Random_Forest.ipynb**
- **6-Regresion_Logistica_Por_Espacio_Poco_Dato.ipynb**

# Archivos del Proyecto
## 1-Descripción del dataset.ipynb
### •	Descripción: Este notebook se encarga de cargar los datos desde el archivo Excel, realizar una Descripción completa del mismo y un Análisis exploratorio visual.
### •	Pasos importantes:
        Carga de los datos.
        Inspección inicial de las primeras filas.
        Obtener información general del data set.
        Realizar estadísticas descrptivas
        Identificación valores únicos
        Análsis exploratorio visula de la Distribución de la variable objetivo, títulos más frecuentes, Espacios curriculares más asignados.
        Visualizar la relación entre clasificación y y los 10 espacios curriculares más frecuentes
## 2-Limpieza y Tratamiento de Datos .ipynb
### •	Descripción: Este notebook se encarga de realizar un plan ETL (Extracción, Transformación y Carga)
### •	Pasos importantes:
        Análisis de valores faltantes
        FILTRADO DE VARIABLES RELEVANTES
        LIMPIEZA DE VALORES NULOS
        convertir a mayúsculas y eliminar espacios en blanco en las columnas de Título, Nombre, Provincia y Desc_espacio para estandarizar los datos.
        Guardar el conjunto de datos limpio en un archivo CSV en una ruta especifica para que pueda ser utilizado en el entrenamiento de modelo.
## 3-Modelo_Regresion_Logistica.ipynb
### •	Descripción: Este notebook entrena el modelo de aprendizaje automático para predecir el Carácter del titulo, como Docente, Habilitante o Supletorio según el titulo, la institución emisora (nombre) y el espacio curricular (desc_espacio)
### •	Pasos importantes:
        Entrenamiento del modelo de regresión Logistica
        Evaluación de la precisión del modelo utilizando métricas estándar

## 4-Arbol_Decision.ipynb
### •	Descripción: Este notebook entrena el modelo de aprendizaje automático para predecir el Carácter del titulo, como Docente, Habilitante o Supletorio según el titulo, la institución emisora (nombre) y el espacio curricular (desc_espacio)
### •	Pasos importantes:
        Entrenamiento del modelo de Arbol de Decision
        Evaluación de la precisión del modelo utilizando métricas estándar
## 5-Modelo_Random_Forest.ipynb
### •	Descripción: Este notebook entrena el modelo de aprendizaje automático para predecir el Carácter del titulo, como Docente, Habilitante o Supletorio según el titulo, la institución emisora (nombre) y el espacio curricular (desc_espacio)
### •	Pasos importantes:
        Entrenamiento del modelo de Random Forest
        Evaluación de la precisión del modelo utilizando métricas estándar

## 6-Regresion_Logistica_Por_Espacio_Poco_Dato.ipynb
### •	Descripción: En este notebook abordé un análisis más específico: aplicar la regresión logística en aquellos espacios curriculares con pocos registros (menos de 100), con el fin de detectar qué espacios curriculares presentan escasez de aspirantes con títulos adecuados.
### •	Pasos importantes:
        Entrenamiento del modelo de Random Forest
        Evaluación de la precisión del modelo utilizando métricas estándar





