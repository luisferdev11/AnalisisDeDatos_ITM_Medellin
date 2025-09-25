import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta de outputs si no existe
output_folder = 'outputs_456'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Carpeta '{output_folder}' creada exitosamente")

# Cargar dataset limpio
df_clean = pd.read_csv("healthcare_clean.csv")

def plot_billing_by_insurance(df):
    """Muestra la carga de costos promedio según aseguradora con valores encima de cada barra."""
    billing_summary = df.groupby('Insurance Provider')['Billing Amount'].mean() \
                        .sort_values(ascending=False)

    plt.figure(figsize=(10,6))
    ax = billing_summary.plot(kind='bar', color='teal')
    plt.title(f"Aseguradoras por Promedio de Facturación")
    plt.xlabel("Aseguradora")
    plt.ylabel("Monto Promedio Facturado")
    plt.xticks(rotation=45, ha="right")

    # Agregar valores encima de cada barra
    for i, v in enumerate(billing_summary.values):
        ax.text(i, v + (billing_summary.max() * 0.01), 
                f"{v:,.0f}", ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Guardar gráfico
    nombre_archivo = f"{output_folder}/billing_by_insurance.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado: {nombre_archivo}")

    return billing_summary



# ---------------------------
# Ejecutar función
# ---------------------------
print("Iniciando análisis de costos por aseguradora...")

billing_summary = plot_billing_by_insurance(df_clean)
