# 📄 Diccionario de Datos Procesados

Este documento detalla las variables contenidas en el dataset final consolidado (`pacientes_processed.csv`), el cual fue construido tras la etapa de ETL y sirve como base para el modelado predictivo del riesgo suicida.

Cada fila representa un paciente único, y las columnas reflejan datos consolidados, recategorizados o generados a partir de cálculos y expresiones sobre los registros clínicos originales.

---

## 📑 `pacientes_processed.csv`

| Columna                         | Tipo de dato       | Descripción                                                                 |
|--------------------------------|--------------------|-----------------------------------------------------------------------------|
| paciente_nro                   | numérico entero    | Identificador único del paciente                                            |
| edad                           | numérico entero    | Edad actual calculada al momento de consolidación                          |
| paciente_sexo                  | texto              | Sexo del paciente                                                           |
| paciente_localidad             | texto              | Localidad de residencia                                                     |
| cobertura_cat                  | texto              | Categoría de cobertura (sin cobertura, estatal, privada)                   |
| n_internaciones                | numérico entero    | Cantidad total de internaciones registradas                                |
| dias_estada_avg                | numérico decimal   | Promedio de días de estadía por internación                                |
| tipo_egreso_mas_frecuente      | texto              | Tipo de egreso más frecuente entre sus internaciones                       |
| internacion_salud_mental      | booleano (0/1)     | Si alguna internación estuvo asociada a especialidades de salud mental     |
| n_diagnosticos                 | numérico entero    | Cantidad total de diagnósticos registrados                                 |
| refiere_ansiedad               | booleano (0/1)     | Mención de ansiedad en texto subjetivo                                     |
| refiere_estres                 | booleano (0/1)     | Mención de estrés en texto subjetivo                                       |
| refiere_insomnio              | booleano (0/1)     | Mención de insomnio en texto subjetivo                                     |
| centro_atencion_mas_frecuente | texto              | Centro de atención más frecuente                                            |
| riesgo_suicida                 | booleano (0/1)     | Variable objetivo: indica riesgo suicida según criterios clínico-textuales |

---

Todas estas variables fueron validadas en términos de consistencia clínica, completitud y relevancia estadística para su uso en modelos de clasificación supervisada.

Se aplicaron codificaciones y técnicas de balanceo sobre esta matriz para optimizar el rendimiento predictivo.
