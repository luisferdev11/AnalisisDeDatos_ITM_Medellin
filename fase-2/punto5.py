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


def plot_age_groups_vs_condition(df):
    """Muestra la enfermedad más común por cada rango de edad (10 en 10)."""
    df = df.copy()
    df['Age Group'] = pd.cut(df['Age'], bins=range(0, df['Age'].max()+10, 10))

    # Encontrar la enfermedad más común en cada grupo
    common_conditions = df.groupby('Age Group', observed=True)['Medical Condition'] \
        .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else "Sin datos")

    # Conteo para graficar
    condition_counts = df.groupby(['Age Group','Medical Condition'], observed=True).size() \
                         .reset_index(name='count')

    plt.figure(figsize=(12,6))
    sns.barplot(data=condition_counts, x='Age Group', y='count', hue='Medical Condition')
    plt.title("Condiciones Médicas más Comunes por Grupo de Edad")
    plt.xlabel("Grupo de Edad (años)")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.legend(title="Condición Médica", bbox_to_anchor=(1.05, 1), loc='upper left')

    nombre_archivo = f"{output_folder}/age_groups_vs_condition.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado: {nombre_archivo}")

    return common_conditions



def plot_stay_length_vs_billing(df):
    """Muestra el monto promedio facturado según la duración de hospitalización."""
    df = df.copy()
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')
    df['Stay Length'] = (df['Discharge Date'] - df['Date of Admission']).dt.days

    # Agrupar por días de hospitalización y calcular promedio
    avg_billing = df.groupby('Stay Length')['Billing Amount'].mean().reset_index()

    plt.figure(figsize=(10,6))
    ax = sns.lineplot(data=avg_billing, x='Stay Length', y='Billing Amount', 
                      marker='o', color='purple')

    plt.title("Promedio de Facturación según Días de Hospitalización")
    plt.xlabel("Días de Hospitalización")
    plt.ylabel("Monto Promedio Facturado")

    # Guardar gráfico
    nombre_archivo = f"{output_folder}/stay_length_vs_billing.png"
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfico guardado: {nombre_archivo}")



# ---------------------------
# Ejecutar funciones
# ---------------------------
print("Iniciando generación de gráficos...")

common_conditions = plot_age_groups_vs_condition(df_clean)
plot_stay_length_vs_billing(df_clean)
