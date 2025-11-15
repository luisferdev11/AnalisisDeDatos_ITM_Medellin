# EJERCICIO 1
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

# EJERCICIO 5

# 📘 Predicción del Abandono de Empleados  
### *Módulo: Modelado Estadístico y Aprendizaje Supervisado*  
### *Proyecto perteneciente a la Cuarta Evaluación*

Este cuaderno forma parte del proyecto de la **Cuarta Evaluación**, enfocado en el análisis de datos de Recursos Humanos con el objetivo de **predecir la probabilidad de abandono de empleados** en una empresa. Utilizando el dataset *HR Analytics Employee Attrition*, se implementan modelos de clasificación para identificar patrones que permitan anticipar la rotación laboral y tomar decisiones preventivas basadas en evidencia.

## 🔬 Descripción Técnica del Análisis

1. **Exploratory Data Analysis (EDA)**  
   - Exploración de variables clave: satisfacción, evaluación, proyectos, horas trabajadas  
   - Análisis de correlaciones, valores extremos y comportamiento por grupo  
   - Estudio del desbalance de clases y tendencias de abandono por salario y antigüedad  

2. **Limpieza y Preprocesamiento de Datos**  
   - Verificación de datos nulos y tratamiento de outliers mediante rango intercuartílico  
   - Codificación one-hot para variables categóricas (`salary`, `Department`)  
   - Estandarización de variables numéricas para PCA y modelos lineales

3. **Entrenamiento de Modelos Supervisados**  
   - **Regresión Logística**  
   - **Árbol de Decisión**  
   - **Random Forest**  
   Cada modelo fue ajustado sobre un conjunto de entrenamiento y debidamente evaluado.

4. **Evaluación y Visualización**  
   - Métricas: **F1-score**, **ROC-AUC** y matrices de confusión  
   - Curvas ROC para comparar rendimiento discriminativo  
   - Visualización de datos reducidos con **PCA**

## 📊 Resultados y Discusión Técnica

El modelo **Random Forest** presentó el mejor rendimiento (F1 ≈ 0.98, ROC-AUC ≈ 0.99), mostrando una alta capacidad para detectar empleados en riesgo de abandono con muy bajo nivel de falsos positivos. El **Árbol de Decisión** también alcanzó un rendimiento alto (F1 ≈ 0.95), mientras que la **Regresión Logística**, aunque más simple, logró AUC de 0.85 con F1 de 0.45, quedando limitada por su linealidad. El análisis de importancia de variables reveló que la **satisfacción laboral**, la **antigüedad** y la **carga de trabajo** fueron los factores más influyentes en la predicción.

## ⚖️ Consideraciones Éticas

El uso de modelos predictivos en recursos humanos debe hacerse con responsabilidad. Se destaca la importancia de no usar estos modelos para discriminar, sino para **ofrecer apoyo proactivo** y mejorar las condiciones laborales. La predicción debe ser transparente, explicable y respetar la privacidad de los empleados. Un mal uso podría generar etiquetas injustas o decisiones automatizadas sin fundamento humano.
