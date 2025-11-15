# ============================================================
# BUILD_FEATURES.PY - Preparación y Feature Engineering
# Proyecto: MOCACI
# ============================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def encode_categorical(df: pd.DataFrame, categorical_cols: list):
    """
    Aplica One-Hot Encoding a las columnas categóricas.
    """
    print("🎛️ Aplicando One-Hot Encoding...")
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=False)
    print(f"✔ Nuevas columnas: {df_encoded.shape[1]}")
    return df_encoded


def scale_numeric(df: pd.DataFrame, numeric_cols: list):
    """
    Escala las columnas numéricas usando StandardScaler.
    """
    print("📐 Escalando columnas numéricas...")

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, scaler


def select_features(df: pd.DataFrame, target_col: str):
    """
    Separa X e y.
    """
    X = df.drop(target_col, axis=1)
    y = df[target_col]

    print(f"📊 Features: {X.shape[1]} columnas")
    print(f"🎯 Target: {target_col}")

    return X, y


def reorder_columns(df: pd.DataFrame, cols: list):
    """
    Ordena las columnas según un orden específico.
    """
    return df[cols]
