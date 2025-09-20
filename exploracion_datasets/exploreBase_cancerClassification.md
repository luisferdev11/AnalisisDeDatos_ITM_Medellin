# Análisis del Dataset: *Medical Text Dataset - Cancer Doc Classification* (Kaggle)

📂 **Fuente:** [Medical Text Dataset - Cancer Doc Classification (Kaggle)](https://www.kaggle.com/datasets/falgunipatel19/biomedical-text-publication-classification), cuyo autor *"Falgunipatel19"*.
📑 **Tipo de datos:** Conjunto de textos biomédicos clasificados (papers y resúmenes de investigación sobre 3 tipos de cancer: tiroides, colon y pulmón).

---

## Origen de los datos

- **Plataforma:** Kaggle.  
- **Enfoque:** Artículos y resúmenes de investigación biomédica (generalmente de más de 6 páginas).  
- **Clasificación:** Secundaria o terciaria, ya que consiste en una compilación pública destinada a fines académicos y no comerciales.  

---

---

## Tipo de datos

Este dataset corresponde a **datos secundarios/terciarios**:

- ❌ **No son primarios**, porque no provienen de una recolección directa de datos clínicos o experimentales.  
- ✅ **Secundarios**, porque recopilan información publicada en artículos y resúmenes biomédicos previamente generados por otros investigadores.  
- ✅ **Terciarios**, porque la recopilación y organización en Kaggle constituye una compilación de datos secundarios en una fuente accesible y estructurada.  

Concluyendo, el dataset es **una fuente secundaria/terciaria**, ideal para fines académicos y experimentación en PLN, pero no para estudios clínicos directos.

---

## Composición del dataset

- **Número total de documentos:** 7,570 artículos de investigación.  
- **Categorías de cáncer incluidas:**
  - **Cáncer de Tiroides (Thyroid_Cancer):** 2,810 documentos.  
  - **Cáncer de Colon (Colon_Cancer):** 2,579 documentos.  
  - **Cáncer de Pulmón (Lung_Cancer):** 2,180 documentos.  

- **Atributos principales:**
  1. `Serial Number` → Identificador único de cada registro.  
  2. `Class Labels` → Etiqueta que indica el tipo de cáncer.  
  3. `Research Paper Text` → Texto completo del artículo o resumen biomédico.  

---

## Nivel de documentación disponible

- **En Kaggle:**  
  La documentación es explícita y bien estructurada, con detalle sobre el número de publicaciones y la distribución por categoría.  

- **En publicaciones/notebooks externos:**  
  Ha sido utilizado en investigaciones y proyectos de clasificación de texto, sirviendo como ejemplos prácticos adicionales.  

- **Limitaciones:**  
  - Se centra en **texto de investigación**, no en historiales clínicos.  
  - Carece de metadatos clínicos adicionales (edad, género, historial médico del paciente).  
  - Esto limita su aplicabilidad a estudios epidemiológicos, aunque es muy útil para NLP y clasificación.  

---

## Posibles aplicaciones

- **Clasificación de documentos biomédicos:**  
  Entrenamiento y evaluación de modelos de *machine learning* y *deep learning* (regresión logística, redes neuronales, modelos transformadores).  

- **Análisis exploratorio de datos (EDA) y Procesamiento de Lenguaje Natural (PLN):**  
  Preprocesamiento de texto, análisis de frecuencia de términos, extracción de tópicos y reducción de dimensionalidad.  

- **Análisis de patrones del lenguaje:**  
  Identificación de terminología y estructuras lingüísticas características en investigaciones de distintos tipos de cáncer.  

---

## Conclusión

Este dataset nos es un recurso sólido para proyectos de clasificación supervisada y experimentación con modelos de texto biomédico. Su mayor valor radica en el volumen y diversidad temática de los documentos, aunque no está orientado a análisis clínicos directos debido a la ausencia de metadatos de pacientes.
