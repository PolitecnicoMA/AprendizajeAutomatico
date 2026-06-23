# 🧠 Evaluación de Modelos

Esta sección documenta el proceso de entrenamiento y evaluación de los modelos supervisados aplicados al problema de detección de riesgo suicida en jóvenes.

---

## 📌 Modelos seleccionados

Se entrenaron dos tipos de modelos supervisados:

* Regresión Logística
* Árbol de Decisión

Cada uno fue probado con y sin técnicas de balanceo de clases para mejorar la sensibilidad del modelo respecto a la clase minoritaria (`riesgo_suicida = 1`).

---

## ⚖️ Estrategia de evaluación

Dado que el objetivo principal del proyecto fue **maximizar la sensibilidad**, se priorizó el `recall` sobre otras métricas. Las métricas evaluadas fueron:

* Accuracy
* Recall (para la clase positiva)
* F1-score

---

## 📊 Resultados

### Regresión logística (sin balanceo)

* Accuracy: 0.92
* Recall (Clase 1): 0.1264
* F1-score (Clase 1): 0.2115

→ El modelo fue incapaz de detectar correctamente la mayoría de los casos positivos. Detectó 22 verdaderos positivos sobre 174, con alta tasa de falsos negativos.

### Regresión logística (con balanceo)

* Accuracy: 0.8108
* Recall (Clase 1): 0.65
* F1-score (Clase 1): 0.37

→ Mejoró significativamente la sensibilidad, captando 113 verdaderos positivos. Aceptable compromiso entre sensibilidad y precisión general.

### Árbol de decisión (con balanceo)

* Accuracy: 0.87
* Recall (Clase 1): 0.32
* F1-score (Clase 1): 0.29

→ Menor recall que la regresión balanceada, pero útil para entender la jerarquía de variables.

#### Variables más relevantes según el árbol:

* `n_diagnosticos`
* `refiere_ansiedad`
* `internacion_salud_mental`
* `cobertura_cat`
* `n_internaciones`
* `centro_atencion_mas_frecuente`

---

## 📈 Comparación general

| Modelo                         | Accuracy | Recall Clase 1 | F1-score Clase 1 |
| ------------------------------ | -------- | -------------- | ---------------- |
| Regresión logística            | 0.92     | 0.13           | 0.21             |
| Regresión logística balanceada | 0.81     | 0.65           | 0.37             |
| Árbol de decisión balanceado   | 0.87     | 0.32           | 0.29             |

---

## ✅ Conclusiones

* La **regresión logística balanceada** fue la mejor estrategia para cumplir el objetivo del proyecto.
* Si bien sacrificó algo de precisión general, logró un recall del 65%, lo que la convierte en una herramienta útil para anticipar riesgos.
* El árbol permitió observar con mayor claridad la lógica de clasificación y la importancia de las variables clínicas y sociales.

---

## 🔭 Proyecciones y líneas futuras

* Aplicar técnicas más avanzadas de sobremuestreo como **SMOTE** o **ADASYN**.
* Probar modelos más complejos como **Random Forest** o **Gradient Boosting**.
* Implementar validación cruzada con conjuntos independientes.
* Analizar secuencias temporales con modelos longitudinales.
* Trabajar colaborativamente con equipos clínicos para validar interpretaciones y ajustar criterios operativos.
