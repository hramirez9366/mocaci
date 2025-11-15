# ============================================================
# LOAD_DATA.PY - Funciones para cargar y validar datos
# Proyecto: MOCACI
# ============================================================

import pandas as pd
import os


def load_raw_data(path: str):
    """
    Carga el dataset RAW desde data/raw/.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ No se encontró el archivo en: {path}")

    df = pd.read_csv(path)
    print(f"✅ Datos RAW cargados correctamente: {df.shape[0]} filas.")
    return df


def load_processed_data(path: str):
    """
    Carga el dataset procesado desde data/processed/.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ No se encontró el archivo procesado en: {path}")

    df = pd.read_csv(path)
    print(f"📦 Datos procesados cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df


def check_missing_values(df: pd.DataFrame):
    """
    Revisa si el dataset contiene valores nulos.
    """
    missing = df.isnull().sum()
    print("🔍 Valores nulos por columna:")
    print(missing)
    return missing


def save_processed_data(df: pd.DataFrame, path: str):
    """
    Guarda un dataset procesado en data/processed/.
    """
    df.to_csv(path, index=False)
    print(f"💾 Dataset procesado guardado en: {path}")