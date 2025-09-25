import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de estilo
plt.style.use('default')
sns.set_palette("husl")

# Crear carpeta de outputs si no existe
output_folder = 'outputs_456'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Carpeta '{output_folder}' creada exitosamente")

# Cargar dataset limpio
df_clean = pd.read_csv("healthcare_clean.csv")

def plot_age_distribution(df):
    """Muestra histograma y curva de densidad de la variable Age."""
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], kde=True, bins=20, color='skyblue')
    plt.title("Distribución de la Edad")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")

    # Guardar gráfico
    nombre_archivo = f"{output_folder}/age_distribution.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado: {nombre_archivo}")


def plot_top_medical_conditions(df):
    """Grafica las enfermedades más comunes en el dataset con totales en las barras."""
    plt.figure(figsize=(10,6))
    
    # Obtener los conteos
    counts = df['Medical Condition'].value_counts()
    
    # Graficar
    ax = counts.plot(kind='bar', color='salmon')
    plt.title("Enfermedades Más Comunes")
    plt.xlabel("Condición Médica")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45, ha="right")
    
    # Poner valores encima de las barras
    for i, v in enumerate(counts.values):
        ax.text(i, v + (max(counts.values) * 0.01), str(v), 
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Guardar gráfico
    nombre_archivo = f"{output_folder}/medical_conditions.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado: {nombre_archivo}")



# ---------------------------
# Ejecutar funciones
# ---------------------------
print("Iniciando gráficos del Punto 4...")

plot_age_distribution(df_clean)
plot_top_medical_conditions(df_clean)

