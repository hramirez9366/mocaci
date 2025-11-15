# ============================================================
# TRAIN.PY - Entrenamiento del modelo MOCACI
# Proyecto: MOCACI - Modelo de Clasificación de Amenazas Cibernéticas
# ============================================================
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, classification_report
)
from sklearn.ensemble import RandomForestClassifier


# ============================================================
# 1. CARGAR DATASET PROCESADO
# ============================================================

DATA_PATH = "data/processed/amenazas_ciberseguridad_prepared.csv"
MODEL_DIR = "models"

print("🔍 Cargando dataset procesado...")
df = pd.read_csv(DATA_PATH)

print(f"✅ Dataset cargado: {df.shape[0]} registros y {df.shape[1]} columnas")


# ============================================================
# 2. SEPARAR FEATURES Y LABEL
# ============================================================

X = df.drop("threat_type", axis=1)
y = df["threat_type"]

print(f"📌 Features: {X.shape}")
print(f"📌 Target: {y.nunique()} clases")


# ============================================================
# 3. DIVISIÓN TRAIN / TEST
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("📊 División completada:")
print(f"- Train: {X_train.shape}")
print(f"- Test:  {X_test.shape}")


# ============================================================
# 4. ESCALADO DE VARIABLES NUMÉRICAS
# ============================================================

numeric_cols = X.select_dtypes(include=[np.number]).columns

scaler = StandardScaler()
X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

print("📐 Variables numéricas escaladas correctamente.")


# ============================================================
# 5. ENTRENAMIENTO DEL MODELO (OPTIMIZADO)
# ============================================================

print("\n🚀 Entrenando modelo Random Forest (versión ligera)...")

model = RandomForestClassifier(
    n_estimators=120,
    max_depth=12,
    min_samples_split=4,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("🎉 Entrenamiento completado.")


# ============================================================
# 6. EVALUACIÓN
# ============================================================

y_pred = model.predict(X_test)

print("\n📊 Métricas de Rendimiento del Modelo:")
print("-----------------------------------------")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-score:  {f1_score(y_test, y_pred, average='weighted'):.4f}")

print("\n🔎 Classification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# 7. GUARDAR MODELO + TRANSFORMADORES
# ============================================================

os.makedirs(MODEL_DIR, exist_ok=True)

model_path = os.path.join(MODEL_DIR, "mocaci_model.pkl")
scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")
columns_path = os.path.join(MODEL_DIR, "feature_columns.pkl")

joblib.dump(model, model_path, compress=3)
joblib.dump(scaler, scaler_path, compress=3)
joblib.dump(list(X.columns), columns_path)

print("\n💾 Archivos guardados:")
print(f"Modelo:         {model_path}")
print(f"Scaler:         {scaler_path}")
print(f"Columnas:       {columns_path}")

print("\n✅ ENTRENAMIENTO COMPLETO")
