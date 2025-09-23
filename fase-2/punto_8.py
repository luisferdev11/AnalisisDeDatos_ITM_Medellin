
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuración básica
DATA_PATH = "./healthcare_dataset.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Identificar tipos de columnas
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
# Detectar columnas de fecha
datetime_cols = []
for col in categorical_cols:
    try:
        parsed = pd.to_datetime(df[col], errors="coerce", infer_datetime_format=True)
        if parsed.notna().mean() > 0.9:
            datetime_cols.append(col)
    except Exception:
        pass
categorical_cols = [c for c in categorical_cols if c not in datetime_cols]

# Histogramas
for col in numeric_cols:
    data = df[col].dropna()
    if data.empty:
        continue
    plt.figure()
    plt.hist(data, bins="auto")
    plt.title(f"Histograma: {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/hist_{col}.png", dpi=150)
    plt.close()

# Boxplots
for col in numeric_cols:
    data = df[col].dropna()
    if data.empty:
        continue
    plt.figure()
    plt.boxplot(data, vert=True, showfliers=True)
    plt.title(f"Boxplot: {col}")
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/box_{col}.png", dpi=150)
    plt.close()

# Barras para categóricas
for col in categorical_cols:
    vc = df[col].astype("category").value_counts().head(15)
    if vc.empty:
        continue
    plt.figure()
    plt.bar(vc.index.astype(str), vc.values)
    plt.title(f"Frecuencias: {col}")
    plt.xlabel(col)
    plt.ylabel("Conteo")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/bar_{col}.png", dpi=150)
    plt.close()

# Dispersión para pares de numéricas
if len(numeric_cols) > 1:
    corr = df[numeric_cols].corr(numeric_only=True)
    pairs = []
    for i, a in enumerate(numeric_cols):
        for j, b in enumerate(numeric_cols):
            if j <= i:
                continue
            val = corr.loc[a, b]
            if pd.notna(val):
                pairs.append((abs(val), a, b))
    pairs.sort(reverse=True)
    for _, a, b in pairs[:5]:
        sub = df[[a, b]].dropna()
        if sub.empty:
            continue
        plt.figure()
        plt.scatter(sub[a], sub[b], s=10)
        plt.title(f"Dispersión: {a} vs {b}")
        plt.xlabel(a)
        plt.ylabel(b)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/scatter_{a}_vs_{b}.png", dpi=150)
        plt.close()

# Mapa de calor de correlaciones
if len(numeric_cols) > 1:
    corr = df[numeric_cols].corr(numeric_only=True)
    plt.figure()
    im = plt.imshow(corr, aspect="auto")
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.title("Mapa de calor de correlaciones")
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45, ha="right")
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/heatmap_correlaciones.png", dpi=150)
    plt.close()

# Series de tiempo si hay columnas datetime
if datetime_cols:
    dt_col = datetime_cols[0]
    dt = pd.to_datetime(df[dt_col], errors="coerce", infer_datetime_format=True)
    ts_df = df.copy()
    ts_df[dt_col] = dt
    ts_df = ts_df.dropna(subset=[dt_col]).sort_values(dt_col)
    for col in numeric_cols[:5]:
        series = ts_df[[dt_col, col]].dropna()
        if series.empty:
            continue
        tmp = series.set_index(dt_col)
        try:
            tmp = tmp.resample("D").mean()
        except Exception:
            pass
        plt.figure()
        plt.plot(tmp.index, tmp[col])
        plt.title(f"Serie de tiempo: {col} vs {dt_col}")
        plt.xlabel(dt_col)
        plt.ylabel(col)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/timeseries_{col}.png", dpi=150)
        plt.close()
