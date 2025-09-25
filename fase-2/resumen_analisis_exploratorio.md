# Análisis Exploratorio de Datos - Dataset Healthcare

## Resumen Ejecutivo

Este documento presenta los resultados del análisis exploratorio inicial del dataset `healthcare_dataset.csv`, incluyendo la revisión de valores faltantes, detección de valores atípicos y análisis de distribuciones de variables numéricas.

## 1. Revisión de Valores Faltantes


✅ **No se encontraron valores faltantes** en ninguna de las columnas del dataset.

Esto indica que el dataset está completo y no requiere tratamiento para datos ausentes.

## 2. Detección de Valores Atípicos

Se analizaron las siguientes variables numéricas utilizando métodos gráficos (box plots) y estadísticos (método IQR):


### Age
✅ **No se detectaron outliers** en esta variable.
- Total de observaciones: 0 outliers
- Porcentaje: 0.00%
- Límites IQR: [-14.50, 117.50]

![Box Plot y Distribución de Age](outputs_puntos123/boxplot_distribucion_age.png)

### Billing Amount
✅ **No se detectaron outliers** en esta variable.
- Total de observaciones: 0 outliers
- Porcentaje: 0.00%
- Límites IQR: [-23627.70, 74689.43]

![Box Plot y Distribución de Billing Amount](outputs_puntos123/boxplot_distribucion_billing_amount.png)

### Room Number
✅ **No se detectaron outliers** en esta variable.
- Total de observaciones: 0 outliers
- Porcentaje: 0.00%
- Límites IQR: [-96.50, 699.50]

![Box Plot y Distribución de Room Number](outputs_puntos123/boxplot_distribucion_room_number.png)

## 3. Análisis de Distribuciones

Se exploró la forma de las variables numéricas mediante histogramas y curvas de densidad:


### Age
- **Media**: 51.54
- **Mediana**: 52.00
- **Desviación Estándar**: 19.60
- **Skewness**: -0.01 (aproximadamente simétrica hacia la izquierda)
- **Kurtosis**: -1.19 (platicúrtica (picos menos pronunciados))

La diferencia entre media (51.54) y mediana (52.00) indica sesgo hacia la izquierda.

![Distribución de Age](outputs_puntos123/distribucion_age.png)

### Billing Amount
- **Media**: 25539.32
- **Mediana**: 25538.07
- **Desviación Estándar**: 14211.45
- **Skewness**: -0.00 (aproximadamente simétrica hacia la izquierda)
- **Kurtosis**: -1.19 (platicúrtica (picos menos pronunciados))

La diferencia entre media (25539.32) y mediana (25538.07) indica sesgo hacia la derecha.

![Distribución de Billing Amount](outputs_puntos123/distribucion_billing_amount.png)

### Room Number
- **Media**: 301.13
- **Mediana**: 302.00
- **Desviación Estándar**: 115.24
- **Skewness**: -0.01 (aproximadamente simétrica hacia la izquierda)
- **Kurtosis**: -1.19 (platicúrtica (picos menos pronunciados))

La diferencia entre media (301.13) y mediana (302.00) indica sesgo hacia la izquierda.

![Distribución de Room Number](outputs_puntos123/distribucion_room_number.png)

## 4. Conclusiones y Recomendaciones

### Hallazgos Principales:

- ✅ **Dataset completo**: No se encontraron valores faltantes en ninguna columna

- ✅ **Sin outliers**: No se detectaron valores atípicos en las variables analizadas

### Recomendaciones:

1. **Limpieza de datos**: El dataset está en buenas condiciones para análisis posteriores
2. **Transformaciones**: Evaluar si las distribuciones sesgadas requieren transformaciones logarítmicas o de Box-Cox
3. **Análisis adicional**: Considerar análisis de correlaciones entre variables numéricas
4. **Validación**: Los outliers detectados (si los hay) deben evaluarse en el contexto del dominio médico

### Próximos Pasos:
- Análisis de variables categóricas
- Análisis de correlaciones
- Preparación de datos para modelado
- Análisis estadístico inferencial

---
# Conclusiones del Análisis Univariado, Multivariado y Entre Variables

## 1. Análisis univariado
- La distribución de enfermedades muestra que **artritis, diabetes e hipertensión** son las más frecuentes en el conjunto de datos, con valores muy cercanos (todas alrededor de 9,200 a 9,300 casos).  
- Este comportamiento refleja que la base de pacientes está altamente concentrada en **condiciones crónicas comunes**, lo cual puede tener implicaciones en la planificación de servicios médicos y políticas de prevención.  

---

## 2. Análisis multivariado
- Al analizar la relación entre **grupos de edad y enfermedades más comunes**, se observa un patrón claro:
  - En la juventud (20–30 años) la **obesidad** es predominante.  
  - En edades medias (40–60 años) destacan la **diabetes** y nuevamente la **obesidad**.  
  - En la vejez (70–90 años) las condiciones más frecuentes son **hipertensión** y **artritis**.  
- Esto evidencia que la **edad está fuertemente asociada al tipo de condición médica predominante**, en línea con lo que se conoce clínicamente: enfermedades metabólicas y crónicas aumentan su frecuencia a medida que avanza la edad.  

- En cuanto a la **duración de la hospitalización frente al costo facturado**, los resultados muestran que el **monto promedio facturado no crece de manera lineal con los días de hospitalización**.  
  - Aunque hay una ligera tendencia al alza en ciertos tramos, existen variaciones que sugieren que la facturación depende también de otros factores (tipo de procedimiento, complejidad del caso, aseguradora).  

---

## 3. Relaciones entre variables
- El análisis de facturación por **aseguradora** muestra que los valores son relativamente homogéneos:  
  - **Medicare y Blue Cross** presentan los promedios más altos (≈ $25,615), seguidos muy de cerca por Aetna, Cigna y UnitedHealthcare (≈ $25,400–25,500).  
- La diferencia entre las aseguradoras es pequeña, pero consistente, lo que podría deberse a negociaciones contractuales o perfiles de pacientes distintos.  

---

## 📌 Conclusión general
El análisis permite identificar tres hallazgos clave:
1. **Alta prevalencia de enfermedades crónicas comunes** (artritis, diabetes, hipertensión) en la población general.  
2. **Relación clara entre edad y tipo de condición predominante**, donde la obesidad destaca en etapas tempranas y la artritis/hipertensión en edades avanzadas.  
3. **Facturación hospitalaria estable entre aseguradoras**, con ligeras variaciones, y una relación no lineal entre días de hospitalización y costos, lo que abre la puerta a estudios sobre eficiencia hospitalaria y estructuras de facturación.  

Estos resultados constituyen una base sólida para investigaciones posteriores orientadas a la **gestión de recursos**, la **prevención de enfermedades crónicas** y la **optimización de costos en el sector salud**.

