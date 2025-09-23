# 📊 Insights del Dataset Healthcare

## 📌 Insights principales
1. **Distribución de variables numéricas:** Algunas variables presentan distribuciones sesgadas, lo que indica presencia de valores extremos.  
2. **Outliers identificados:** Los boxplots muestran valores atípicos en varias métricas clínicas (ej. medicación, condición médica y gastos médicos).  
3. **Categorías dominantes:** En variables categóricas como género o tipo de sangre, algunas categorías concentran la mayor parte de los registros.  
4. **Correlaciones significativas:** El mapa de calor refleja asociaciones moderadas entre ciertas variables clínicas (ej. edad y costos).  
5. **Volumen y balance:** El dataset es grande (55.501 registros, con 49.992 valores únicos y 15 columnas) y permite un análisis robusto, aunque algunas clases están desbalanceadas.  

---

## ⚠️ Problemas de calidad de datos
- **Valores nulos** presentes en varias columnas.  
- **Categorías con muy baja frecuencia** que podrían afectar modelos predictivos.  
- **Posibles errores de registro**, reflejados en outliers poco realistas (ej. edades o métricas clínicas anómalas).  

---

## 🔮 Posibles líneas de análisis posteriores
- **Modelado predictivo:** Clasificación o regresión para predecir costos o diagnósticos.  
- **Segmentación de pacientes:** Clustering para encontrar perfiles de riesgo o patrones de consumo de salud.  
- **Análisis temporal:** Si las variables de fecha se consolidan, se pueden estudiar tendencias en el tiempo.  
- **Optimización de features:** Ingeniería de variables para reducir sesgos y mejorar el poder explicativo.  
- **Análisis comparativo:** Explorar diferencias entre géneros o grupos de edad en métricas clínicas y económicas.  