# 🔍 Análisis Exploratorio de Datos

Este análisis tuvo como finalidad comprender las características generales de la población incluida en el dataset y detectar posibles patrones relevantes que pudieran incidir en el fenómeno del riesgo suicida.

## Distribución de la variable objetivo

La variable `riesgo_suicida` se construyó como binaria (0/1) a partir del contenido de los campos subjetivos. Representa casos en los que se explicitó ideación, intento o riesgo suicida.

| Clase          | Porcentaje |
| -------------- | ---------- |
| Positiva (`1`) | 8.5%       |
| Negativa (`0`) | 91.5%      |

> Se trata de una variable **altamente desbalanceada**, lo que motivó estrategias de remuestreo durante el modelado.

## Rango temporal

Se incluyeron registros entre **2018 y 2024**, permitiendo observar variaciones en contextos como el aislamiento por COVID-19.

## Centros de atención más frecuentes

* **HRU (Hospital Regional Ushuaia)**
* **HRRG (Hospital Regional Río Grande)**

Estas instituciones concentraron la mayor cantidad de registros.

## Cobertura médica

| Categoría     | Descripción                                |
| ------------- | ------------------------------------------ |
| Sin cobertura | Pacientes sin obra social ni prepaga       |
| Estatal       | OSEF, PAMI, etc.                           |
| Privada       | Cobertura mediante obras sociales privadas |

> Más del **60%** de los pacientes no contaban con cobertura formal.

## Síntomas subjetivos detectados

Se generaron variables binarias a partir de expresiones regulares aplicadas sobre campos subjetivos:

| Variable           | Presencia en el dataset |
| ------------------ | ----------------------- |
| `refiere_ansiedad` | 16.8%                   |
| `refiere_estres`   | 6.1%                    |
| `refiere_insomnio` | 4.2%                    |

Estas variables resultaron informativas durante el modelado.

## Casos extremos detectados

* Hasta **700 diagnósticos** en un mismo paciente.
* Más de **200 internaciones** en algunos casos.

Se aplicaron controles de consistencia para evitar distorsiones.

## Depuración de variables

* Variables con **>60% de nulos** fueron descartadas.
* En otros casos se imputó con la categoría **"SIN DATOS"**.

## Visualizaciones utilizadas

* Histogramas de edad
* Barras por cobertura y centro de atención
* Boxplots por internaciones y diagnósticos

Las visualizaciones permitieron detectar outliers, sesgos en las distribuciones y validar la construcción de variables.

## Hallazgos clave

* Alta proporción de pacientes sin cobertura.
* Predominio de síntomas como ansiedad y estrés en los casos positivos.
* Concentración institucional marcada (HRU y HRRG).
* Fuerte desbalance de la variable objetivo, que justificó el remuestreo.

---

Este análisis guió la selección de variables para el modelado y puso en evidencia factores relevantes desde el punto de vista clínico y social.
