# ============================================================
# VISUALIZE.PY - Gráficos y visualizaciones para MOCACI
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import ConfusionMatrixDisplay


sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


# ---------------------------------------------
# Histogramas y distribuciones
# ---------------------------------------------
def plot_distribution(df: pd.DataFrame, col: str, title: str):
    sns.histplot(df[col], kde=True, bins=40)
    plt.title(title)
    plt.show()


def plot_count(df: pd.DataFrame, col: str, title: str):
    sns.countplot(x=df[col], palette="viridis")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()


# ---------------------------------------------
# Matriz de correlación
# ---------------------------------------------
def plot_correlation(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=False, cmap="coolwarm")
    plt.title("Matriz de Correlación")
    plt.show()


# ---------------------------------------------
# PCA embeddings (dos componentes)
# ---------------------------------------------
def plot_pca(df: pd.DataFrame, labels, title="PCA de Features"):
    pca = PCA(n_components=2)
    components = pca.fit_transform(df)

    plt.scatter(components[:, 0], components[:, 1], c=labels, cmap="tab10", alpha=0.7)
    plt.colorbar()
    plt.title(title)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()


# ---------------------------------------------
# Matriz de confusión
# ---------------------------------------------
def plot_confusion_matrix(model, X_test, y_test, labels):
    disp = ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        display_labels=labels,
        cmap="viridis"
    )
    plt.title("Matriz de Confusión")
    plt.xticks(rotation=45)
    plt.show()
