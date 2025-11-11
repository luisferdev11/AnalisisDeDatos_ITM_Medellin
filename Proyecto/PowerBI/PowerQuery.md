# 📊 Análisis de Datos en Power BI con Power Query
## Proyecto: Auditoría del Dataset de Rayos X - Neumonía (Kaggle)

### 🩺 Contexto del Dataset
El dataset **Chest X-Ray Images (Pneumonia)**, obtenido de Kaggle, contiene imágenes de radiografías de tórax pediátricas clasificadas en **NORMAL** y **PNEUMONIA**

Cada imagen representa un caso médico y está destinada a entrenar, validar y probar modelos de clasificación de neumonía mediante técnicas de aprendizaje automático

---

## ⚙️ Objetivo del Proceso en Power Query

El propósito fue **preparar, limpiar y enriquecer los datos del dataset** utilizando **Power Query** dentro de **Power BI**, con el fin de generar métricas e indicadores que permitan:

- Evaluar la **distribución y balance de clases** (NORMAL vs PNEUMONIA)
- Analizar la **estructura de los conjuntos** (train, test, val)
- Revisar la **calidad de los datos**, incluyendo tamaños de archivo y posibles duplicados
- Preparar la información para el **análisis en Power BI** y la creación de un dashboard de inteligencia de negocios

---

## 🧩 Pasos Realizados en Power Query

### 1. Cargar los Datos desde la Carpeta Raíz
- Se seleccionó la carpeta principal `chest_xray/`

- Luego se eligió la opción **"Transformar datos"** para abrir el editor de Power Query

### 2. Selección de Columnas Relevantes
Se conservaron las siguientes columnas:
- **Content** (binario del archivo)
- **Name** (nombre del archivo)
- **Folder Path** (ruta completa)
- **Date created**
- **Date modified**

Estas columnas permiten identificar la ubicación, el contenido y la fecha de cada imagen

---

## 🧠 Derivación de Nuevas Columnas

### 🔹 a) Columna `Split`
Identifica a qué conjunto pertenece la imagen: `train`, `test` o `val`

```
let
  p = Text.Replace([FolderPath], "/", "\"),
  parts = List.Select(Text.Split(p, "\"), each _ <> ""),
  split = if List.Count(parts) >= 2 then parts{List.Count(parts)-2} else null
in
  split
```

### 🔹 b) Columna `Label`
Determina la etiqueta de clase: NORMAL o PNEUMONIA`

let
    p = Text.Replace([FolderPath], "/", "\"),
    parts = List.Select(Text.Split(p, "\"), each _ <> ""),
    label = if List.Count(parts) >= 1 then parts{List.Count(parts)-1} else null
in
    label

### 🔹 c) Columna `SubType`
Permite identificar subtipos dentro de la clase PNEUMONIA: Bacteria, Virus o null

let
    n = Text.Lower([FileName])
in
    if Text.Contains(n, "bacteria") then "Bacteria"
    else if Text.Contains(n, "virus") then "Virus"
    else null

### 🔹 d) Columna `SizeKB`
Calcula el tamaño de cada archivo en kilobyte

Number.Round(Binary.Length([Content]) / 1024, 2)

### 🔹 e) Columna `BinaryHash`
Genera un código hash único por cada imagen, útil para detectar duplicados

Binary.ToText(Binary.Hash([Content], "MD5"), BinaryEncoding.Hex)


## 🧠 Medidas DAX clave que utilizamos

-- Conteos básicos
Total Imágenes = COUNTROWS(Images)
Total NORMAL = CALCULATE([Total Imágenes], Images[Label] = "NORMAL")
Total PNEUMONIA = CALCULATE([Total Imágenes], Images[Label] = "PNEUMONIA")

-- % por clase (respeta filtros)
% NORMAL = DIVIDE([Total NORMAL], [Total Imágenes])
% PNEUMONIA = DIVIDE([Total PNEUMONIA], [Total Imágenes])

-- Conteos por split para KPIS
Total Train = CALCULATE([Total Imágenes], Images[Split] = "train")
Total Test  = CALCULATE([Total Imágenes], Images[Split] = "test")
Total Val   = CALCULATE([Total Imágenes], Images[Split] = "val")

-- Desbalance (PNEUMONIA : NORMAL) como ratio
Ratio PNEU:NORM = DIVIDE([Total PNEUMONIA], [Total NORMAL])

-- Duplicados por hash
Archivos Duplicados = 
VAR uniq = DISTINCTCOUNT(Images[BinaryHash])
RETURN [Total Imágenes] - uniq

-- Tamaño promedio (KB)
Tamaño Promedio (KB) = AVERAGE(Images[SizeKB])

-- % Subtipo
% Bacteria = DIVIDE(CALCULATE([Total Imágenes], Images[Subtype]="Bacteria"), [Total Imágenes])
% Virus    = DIVIDE(CALCULATE([Total Imágenes], Images[Subtype]="Virus"), [Total Imágenes])


## Enlace de Dashboard
https://app.powerbi.com/groups/me/reports/fef12279-9c3c-49e7-b213-72c173f1fd8c?pbi_source=desktop
