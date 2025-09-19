# Análisis del dataset: Brain Tumor Dataset (Kaggle - ishans24)

## Origen y tipo de datos

- **Fuente:** Dataset disponible en [Kaggle](https://www.kaggle.com/datasets/ishans24/brain-tumor-dataset) bajo el nombre *“Brain Tumor Dataset”* por el usuario *ishans24*.  
  También incluye datos recopilados desde fuentes públicas como [Figshare](https://figshare.com/) y otros repositorios.
- **Composición:** Colección unificada de imágenes de resonancia magnética (MRI), del tipo **T1 ponderadas con contraste**, de distintos tumores cerebrales.  
- **Tipo:** Datos **primarios**, en tanto que corresponden a imágenes médicas originales (MRI). Aunque integran datos de múltiples fuentes, no es un simple resumen o derivado, sino una integración de estudios.

---

## Características básicas

- **Número de registros / imágenes:** 3,064 imágenes de resonancia magnética con contraste T1.  
- **Clases / tipos de tumores:**  
  - Glioma  
  - Meningioma  
  - Pituitario  
  - Sin tumor  
- **Pacientes:** Datos obtenidos de **233 pacientes**.  
- **Tamaño / peso:** 906.29 MB 
- **Atributos:**  
  - Imágenes en formato estándar (JPG/PNG).  
  - Etiquetas de clase asociadas.  
  - **No incluye metadatos clínicos detallados** (edad, sexo, historial, protocolo de adquisición, etc.).  

---

## Nivel de documentación disponible

- **En Kaggle:** Se ofrece una descripción general del dataset (número de imágenes, clases, origen aproximado).  
- **En publicaciones científicas:** Existen papers y reportes que utilizan este dataset, mostrando su uso en clasificación automática de tumores y benchmarks de modelos de deep learning.  
- **Limitaciones en documentación:**  
  - No se detallan metadatos clínicos por paciente (edad, sexo, antecedentes).  
  - No se describe el protocolo de adquisición MRI (campo magnético, resolución exacta, número de cortes).  
  - No se explicita el preprocesamiento aplicado más allá de mencionar limpieza básica e imágenes T1 con contraste.  

---

## Posibles aplicaciones

- Clasificación de tumores cerebrales a partir de imágenes MRI.  
- Entrenamiento de modelos de *machine learning* y *deep learning* (CNNs) para diagnóstico asistido.  
- Benchmark de arquitecturas de redes neuronales aplicadas a imagen médica.  
- Comparación de algoritmos de preprocesamiento y técnicas de balanceo de clases.  
- Potencial uso en herramientas de apoyo clínico, **aunque limitado** por la falta de metadatos clínicos completos.  

---
