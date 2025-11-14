# 📘 Predicción del Rendimiento Académico  
### *Módulo: Modelado Estadístico y Aprendizaje Supervisado*  
### *Proyecto perteneciente a la Cuarta Evaluación*

Este cuaderno forma parte del proyecto integral de la **Cuarta Evaluación**, compuesto por dos trabajos complementarios. En este primer módulo se aborda la problemática de la **predicción del rendimiento académico** a partir del dataset *Student Grade Prediction*, con el propósito de analizar patrones educativos y evaluar la capacidad de distintos algoritmos de clasificación para anticipar el desempeño estudiantil en tres niveles: **alto**, **medio** y **bajo**.

## 🔬 Descripción Técnica del Análisis

1. **Exploratory Data Analysis (EDA)**  
   - Evaluación de la estructura del dataset  
   - Distribución de variables académicas y conductuales  
   - Análisis de correlaciones, outliers y balance de clases  
   - Identificación de relaciones significativas que aportan valor predictivo

2. **Preprocesamiento y Construcción de Etiquetas**  
   - Limpieza, codificación y normalización de variables  
   - Transformación de la nota final (G3) en etiquetas categóricas: *bajo*, *medio*, *alto*  
   - Generación de un conjunto listo para modelos lineales y no lineales

3. **Entrenamiento de Modelos Supervisados**  
   - **Regresión Logística**  
   - **K-Nearest Neighbors (KNN)**  
   - **Support Vector Machines (SVM)**  
   Cada modelo se ajustó y evaluó de manera independiente para analizar su estabilidad y capacidad de generalización.

4. **Evaluación y Visualización**  
   - Métricas: Accuracy, Precision, Recall y F1-score  
   - Reducción de dimensionalidad con **PCA** y **t-SNE**  
   - Curvas ROC multiclase para comparar desempeño discriminativo

## 📊 Resultados y Discusión Técnica

La **Regresión Logística** mostró el mejor desempeño global (≈80%), indicando que las relaciones predictivas dentro del dataset pueden ser modeladas de forma efectiva mediante estructuras lineales y bien regularizadas. En contraste, **KNN** presentó sensibilidad al ruido y a la alta dimensionalidad (≈62%), mientras que **SVM** logró una mejora moderada (≈71%) pero sin superar al modelo lineal. Estos resultados sugieren que, para este caso de estudio, la eficiencia algorítmica proviene más de un *preprocesamiento sólido* y del entendimiento estructural de los datos que del uso de modelos complejos.

## ⚖️ Consideraciones Éticas

El proyecto incorpora una reflexión sobre el uso de sistemas de predicción educativa, enfatizando riesgos como la posible reproducción de desigualdades académicas y la interpretación reduccionista del desempeño estudiantil. Se subraya la necesidad de utilizar estas herramientas únicamente con fines de apoyo, garantizando transparencia, privacidad y no discriminación.
