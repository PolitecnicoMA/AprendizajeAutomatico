## Figures

Este directorio contiene las visualizaciones generadas a partir del análisis del proyecto de predicción de captura de merluza negra en Tierra del Fuego.

---

##  Imágenes incluidas

| Archivo                          | Descripción                                                        |
|----------------------------------|---------------------------------------------------------------------|
| `captura_vs_anomalia.png`        | Dispersión entre la captura mensual y la anomalía de temperatura. |
| `mae_por_modelo.png`             | Comparación del MAE entre modelos (SVM, Random Forest, etc.).     |

---

## captura_vs_anomalia.png
¿Qué muestra?
Un gráfico de dispersión entre la anomalía de temperatura del mar (SST) y la cantidad de merluza negra capturada por mes.

¿Para qué sirve?
-
Para observar si existe relación visual entre las condiciones del océano y las capturas.

Por ejemplo, si al aumentar la temperatura disminuye la captura, podría haber una correlación negativa.

## Interpretación rápida:
Cuando la anomalía de temperatura sube, la captura de merluza tiende a bajar → esto puede sugerir sensibilidad al cambio térmico.

## mae_por_modelo.png

¿Qué muestra?
-
Un gráfico de barras comparando el MAE (error absoluto medio) entre distintos modelos de predicción:

SVM

Random Forest

KNN

¿Para qué sirve?
-
Para saber qué modelo predice mejor (el de menor MAE).

## MAE mide cuántos kilos en promedio se equivoca el modelo al predecir.

## Interpretación rápida:
El modelo con menor barra (en este caso, Random Forest) es el más preciso.
SVM tiene mayor error → peor ajuste al problema.

---
##  Instrucciones

- Todas las imágenes deben tener un nombre claro y estar en formato `.png` o `.jpg`.
- Usar nombres con guiones bajos (`_`) y en minúsculas.
- Las imágenes pueden ser referenciadas directamente en el informe (`report/final_report.md` o `.pdf`).

---

##  Recomendación

Usá este script para guardar tus visualizaciones directamente aquí desde el notebook:

```python
import matplotlib.pyplot as plt

plt.savefig("report/figures/captura_vs_anomalia.png", dpi=300)
```

---

##  Autor

Cristian Couto – Proyecto: Predicción de Captura de Merluza Negra (2025)
