import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración para guardar plots
plt.style.use('default')
sns.set_palette("husl")

# Crear carpeta para outputs si no existe
output_folder = 'outputs_puntos123'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Carpeta '{output_folder}' creada exitosamente")

# Cargar los datos
print("Cargando dataset...")
df = pd.read_csv('healthcare_dataset.csv')
print(f"Dataset cargado: {df.shape[0]} filas y {df.shape[1]} columnas")
print("\nPrimeras 5 filas:")
print(df.head())

def revisar_valores_faltantes(df):
    """
    Identifica variables con datos ausentes, cuantifica la magnitud del problema
    y muestra los resultados.

    Args:
        df: pandas DataFrame
    """
    print("\n=== REVISION DE VALORES FALTANTES ===")
    
    valores_faltantes_count = df.isnull().sum()
    valores_faltantes_porcentaje = (valores_faltantes_count / len(df)) * 100

    valores_faltantes_df = pd.DataFrame({
        'Nombre_Columna': valores_faltantes_count.index,
        'Cantidad_Faltantes': valores_faltantes_count.values,
        'Porcentaje_Faltantes': valores_faltantes_porcentaje.values
    })

    valores_faltantes_df = valores_faltantes_df[valores_faltantes_df['Cantidad_Faltantes'] > 0]
    valores_faltantes_df = valores_faltantes_df.sort_values(by='Porcentaje_Faltantes', ascending=False)

    if len(valores_faltantes_df) == 0:
        print("✓ No se encontraron valores faltantes en el dataset")
    else:
        print("Valores faltantes encontrados:")
        display(valores_faltantes_df)
    
    return valores_faltantes_df

def detectar_valores_atipicos(df, columnas_numericas):
    """
    Emplea métodos gráficos y estadísticos para reconocer posibles outliers
    en columnas numéricas y guarda los plots.

    Args:
        df: pandas DataFrame
        columnas_numericas: Lista de nombres de columnas numéricas a analizar
    """
    print("\n=== DETECCION DE VALORES ATIPICOS ===")
    
    resultados_outliers = {}
    
    for col in columnas_numericas:
        print(f"\nAnalizando columna: {col}")

        # Método gráfico: Box plot
        plt.figure(figsize=(12, 6))
        
        # Crear subplot con box plot y histograma
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Box plot
        sns.boxplot(data=df, y=col, ax=ax1)
        ax1.set_title(f'Box Plot - {col}')
        ax1.set_ylabel(col)
        
        # Histograma
        sns.histplot(data=df, x=col, kde=True, bins=30, ax=ax2)
        ax2.set_title(f'Distribucion - {col}')
        ax2.set_xlabel(col)
        ax2.set_ylabel('Frecuencia')
        
        plt.tight_layout()
        
        # Guardar plot
        nombre_archivo = f"{output_folder}/boxplot_distribucion_{col.lower().replace(' ', '_')}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Plot guardado: {nombre_archivo}")

        # Método estadístico: IQR
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
        
        resultados_outliers[col] = {
            'cantidad_outliers': len(outliers),
            'porcentaje_outliers': (len(outliers) / len(df)) * 100,
            'limite_inferior': limite_inferior,
            'limite_superior': limite_superior,
            'Q1': Q1,
            'Q3': Q3,
            'IQR': IQR
        }

        print(f"Outliers detectados usando IQR: {len(outliers)} ({(len(outliers)/len(df)*100):.2f}%)")
        if len(outliers) > 0:
            print(f"Límites IQR: [{limite_inferior:.2f}, {limite_superior:.2f}]")
    
    return resultados_outliers

def analizar_distribuciones(df, columnas_numericas):
    """
    Explora la forma de las variables numéricas mediante histogramas y gráficas de densidad.

    Args:
        df: pandas DataFrame
        columnas_numericas: Lista de nombres de columnas numéricas a analizar
    """
    print("\n=== ANALISIS DE DISTRIBUCIONES ===")
    
    resultados_distribuciones = {}
    
    for col in columnas_numericas:
        print(f"\nAnalizando distribucion de: {col}")

        # Crear plot con histograma y curva de densidad
        plt.figure(figsize=(12, 6))
        
        # Histograma con curva de densidad
        sns.histplot(data=df, x=col, kde=True, bins=30, alpha=0.7)
        plt.title(f'Distribucion de {col}', fontsize=14, fontweight='bold')
        plt.xlabel(col, fontsize=12)
        plt.ylabel('Frecuencia / Densidad', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Calcular estadísticas de la distribución
        media = df[col].mean()
        mediana = df[col].median()
        desviacion_std = df[col].std()
        skewness = df[col].skew()
        kurtosis = df[col].kurtosis()
        
        # Agregar líneas de referencia
        plt.axvline(media, color='red', linestyle='--', alpha=0.8, label=f'Media: {media:.2f}')
        plt.axvline(mediana, color='green', linestyle='--', alpha=0.8, label=f'Mediana: {mediana:.2f}')
        plt.legend()
        
        # Guardar plot
        nombre_archivo = f"{output_folder}/distribucion_{col.lower().replace(' ', '_')}.png"
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Plot guardado: {nombre_archivo}")
        
        resultados_distribuciones[col] = {
            'media': media,
            'mediana': mediana,
            'desviacion_std': desviacion_std,
            'skewness': skewness,
            'kurtosis': kurtosis
        }
        
        print(f"Estadísticas: Media={media:.2f}, Mediana={mediana:.2f}, Skewness={skewness:.2f}")
    
    return resultados_distribuciones


# Ejecutar análisis
print("Iniciando análisis exploratorio de datos...")

# 1. Revisión de valores faltantes
resultados_faltantes = revisar_valores_faltantes(df)

# 2. Detección de valores atípicos
columnas_numericas = ['Age', 'Billing Amount', 'Room Number']
resultados_outliers = detectar_valores_atipicos(df, columnas_numericas)

# 3. Análisis de distribuciones
resultados_distribuciones = analizar_distribuciones(df, columnas_numericas)

print("\n¡Análisis completado exitosamente!")
print(f"Todos los outputs se han guardado en la carpeta: {output_folder}/")
