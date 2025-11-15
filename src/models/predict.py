# ============================================================
# PREDICT.PY - Predicciones con el modelo MOCACI
# Proyecto: MOCACI - Modelo de Clasificación de Amenazas Cibernéticas
# ============================================================

import pandas as pd
import numpy as np
import joblib
import os

# ============================================================
# 1. CARGAR MODELO, SCALER Y COLUMNAS
# ============================================================

MODEL_PATH = "models/mocaci_model.pkl"
SCALER_PATH = "models/scaler.pkl"
COLUMNS_PATH = "models/feature_columns.pkl"

print("🔍 Cargando modelo y transformadores...")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_columns = joblib.load(COLUMNS_PATH)

print("✅ Modelo cargado correctamente.")


# ============================================================
# 2. FUNCIÓN DE PREDICCIÓN
# ============================================================

def preprocess_input(data: dict):
    """
    Convierte un diccionario en un DataFrame con las columnas correctas,
    aplica one-hot encoding para variables categóricas
    y aplica escalado a variables numéricas.
    """
    # Convertir a DataFrame
    df_input = pd.DataFrame([data])

    # Asegurar que las columnas coincidan con el modelo
    missing_cols = [col for col in feature_columns if col not in df_input.columns]
    for col in missing_cols:
        df_input[col] = 0  # columnas dummy que no vienen en el input

    # Ordenar columnas
    df_input = df_input[feature_columns]

    # Escalar numéricas
    numeric_cols = df_input.select_dtypes(include=[np.number]).columns
    df_input[numeric_cols] = scaler.transform(df_input[numeric_cols])

    return df_input


def predict_threat(data: dict):
    """
    Recibe un diccionario con los datos de un evento
    y devuelve la predicción del tipo de amenaza.
    """
    processed = preprocess_input(data)
    prediction = model.predict(processed)[0]
    probability = np.max(model.predict_proba(processed))

    return prediction, probability


# ============================================================
# 3. PRUEBA LOCAL (solo cuando ejecutes este script)
# ============================================================

if __name__ == "__main__":
    
    print("\n📌 EJEMPLO DE PREDICCIÓN\n")

    # Ejemplo realista basado en tu dataset
    nuevo_evento = {
        "hour": 14,
        "day": 2,
        "month": 7,
        "year": 2023,
        "packet_size": 450,
        "protocol_TCP": 1,
        "protocol_UDP": 0,
        "protocol_ICMP": 0,
        "country_USA": 1,
        "country_Russia": 0,
        "country_China": 0,
        "country_Mexico": 0,
        "country_Brazil": 0,
        # agrega aquí más columnas según tu dataset procesado
    }

    print("🔎 Datos del evento:")
    for k, v in nuevo_evento.items():
        print(f"   - {k}: {v}")

    pred, prob = predict_threat(nuevo_evento)

    print("\n🎯 RESULTADO DE LA PREDICCIÓN")
    print(f"Tipo de amenaza: {pred}")
    print(f"Probabilidad:   {prob:.4f}\n")