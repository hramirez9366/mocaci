# 🔐 MOCACI — Modelo de Clasificación de Amenazas Cibernéticas

Sistema inteligente que identifica y clasifica amenazas cibernéticas automáticamente, mejorando la detección temprana, reduciendo los tiempos de respuesta en un 40% y disminución de falsos positivos en un 25% mediante técnicas de Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![ML](https://img.shields.io/badge/Modelo-ML%20Classification-purple)
![Dataset](https://img.shields.io/badge/Dataset-amenazas_ciberseguridad_v1.csv-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Problema

Los servicios digitales de la institución sufren caídas y riesgos operativos debido a la detección lenta y manual de amenazas cibernéticas. La falta de automatización genera retrasos en la respuesta y aumenta la vulnerabilidad ante ataques dirigidos.

## 💡 Solución

MOCACI propone un modelo de clasificación automática de amenazas cibernéticas entrenado con datos simulados de la institución (2019–2024):
- Clasifica automáticamente eventos de seguridad.
- Reduce la carga manual del equipo de ciberseguridad.
- Permite priorizar amenazas reales.
- Fortalece la respuesta institucional.

## ✨ Características

Lista las funcionalidades clave:
- 🛡️ Clasificación automática de amenazas cibernéticas
- 📥 Procesamiento de eventos de red institucionales
- 🤖 Modelo de Machine Learning entrenado con datos reales simulados (2019–2024)
- 📊 Cálculo de probabilidades por clase
- ⚠️ Reducción de falsos positivos
- 🚀 Diseñado para integrarse a futuro
- 🔄 Pipeline básico de preprocesamiento

## 🛠️ Tecnologías

**Backend & Data Processing:** 
- Python 3.10+
- Pandas
- NumPy

**Machine Learning:**
- Scikit-learn
- Modelos de clasificación (Random Forest, Gradient Boosting)
- Técnicas de división de datos, evaluación y optimización básica

**Datos:**
- rchivo CSV: amenazas_ciberseguridad_v1.csv
- Features generados de tráfico institucional 

**Visualización y Análisis:**
- Matplotlib
- Seaborn
- PCA para visualización de embeddings

**DevOps / Control de Versiones:**
- Git
- GitHub (repositorio del proyecto mocaci)

## 📁 Estructura del Proyecto
```bash
mocaci/
│
├── data/
│   ├── raw/                      
│   │   └── amenazas_ciberseguridad_v1.csv          # Dataset original
│   └──  processed/                                 # Datos limpios y transformados
│       └── amenazas_ciberseguridad_prepared.csv    # Dataset procesado
│
├── notebooks/
│   ├── 01_exploracion_datos.ipynb                  # Exploración y análisis de datos
│   ├── 02_preprocesamiento.ipynb                   # Limpieza y feature engineering
│   └── 03_modelo_clasificacion.ipynb               # Entrenamiento y evaluación del modelo
│
├── src/
│   ├── data/                     
│   │   └── load_data.py                            # Funciones para cargar y preparar datos
│   ├── features/                 
│   │   └── build_features.py                       # Transformaciones y selección de features
│   ├── models/                   
│   │   ├── train.py                                # Script de entrenamiento del modelo
│   │   └── predict.py                              # Script para hacer predicciones con nuevos datos
│   └── visualization/            
│       └── visualize.py                            # Gráficos, PCA, métricas
│
├── models/
│   └── random_forest_mocaci.7z                     # Modelo entrenado, comprimido contiene el archivo pkl
│
├── docs/                                           # Documentación adicional del proyecto
│   └── Documento_Proyecto.pdf                      # Documento formal a entregar
│   └── Presentacion_Proyecto.ppt                   # Presentacion en Power Point
│   └── DATA_DICTIONARY.md                          # Diccicionario de datos
│   └── MODEL_CARD.md                               # Ficha Tecnica del modelo
│   └── PROJECT_CHARTER.md                          # Construccion del proyecto
│
├── requirements.txt                                # Dependencias del proyecto
├── README.md
└── .gitignore
```
## 🚀 Instalación

### Prerequisitos
- Python 3.10 o superior
- pip
- Git
- (Opcional) Entorno virtual recomendado

### Pasos de instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/hramirez9366/mocaci.git
cd mocaci
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate        # Linux / Mac

venv\Scripts\activate           # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Descargar el modelo entrenado (Opcional) 
Si ya existe un modelo guardado:
```bash
mkdir models                    #colocar best_model.pkl dentro de /models
```

5. Ejecutar notebooks o scripts
Para abrir los notebooks:
```bash
jupyter notebook
```
O para hacer una predicción directa:
```bash
python src/models/predict.py
```

## 📊 Resultados

- Accuracy General: 0.84
- Precision Macro: 0.82
- Recall Macro: 0.83
- F1-Score Macro: 0.82
- Matriz de Confusión

## 🗺️ Roadmap

### Versión Actual (v1.0 - MVP)
- [✓] Dataset institucional simulado (amenazas_ciberseguridad.csv)
- [✓] Exploración y análisis de datos (EDA)
- [✓] Peprocesamiento y feature engineering
- [✓] Entrenamiento de modelo de clasificación (Random Forest / Gradient Boosting)
- [✓] Notebook demostrativo para predicción
- [✓] Scripts básicos de carga, predicción y visualización

### Próximas Versiones (v1.1+ / Futuro)
- Integración del modelo con API REST
- Implementación en servidor institucional o Docker
- Dashboard interactivo (Streamlit o Grafana)
- Incorporación de logs reales del firewall / Cloudflare
- Entrenamiento incremental (“online learning”)
- Mejorar soporte para predicciones en tiempo real
- Sistema interno de alertas automáticas basado en probabilidades
- Validación con analistas de ciberseguridad de la institución
- Ajuste de hiperparámetros y modelos más complejos (XGBoost, LightGBM)

## 🤝 Contribución

¡Las contribuciones son bienvenidas!
1. Haz fork del repositorio

2. Crea una rama nueva:
```bash
git checkout -b feature/NuevaCaracteristica
```

3. Realiza tus cambios y documenta adecuadamente
```bash
git commit -m "Add: Nueva característica"
```

4. Sube tus cambios:
```bash
git push origin feature/NuevaCaracteristica
```

5. Abre un Pull Request en GitHub

## 👥 Equipo

- **Henry Ramirez** - Data Scientist / Analista de Ciberseguridad - [@hramirez9366](https://github.com/hramirez9366)
- **Juan Laug** - Ingeniero de Datos / Analista de Ciberseguridad - [@juanlaug111](https://github.com/)

## 📧 Contacto

- Email: notificaciones.henryramirez@gmail.com
