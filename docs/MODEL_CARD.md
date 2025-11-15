# 🧠 Model Card — MOCACI (Modelo de Clasificación de Amenazas Cibernéticas)

Este documento describe el modelo entrenado, sus objetivos, rendimiento y limitaciones.

## 1. Descripción del Modelo
MOCACI es un modelo de **clasificación multiclase** diseñado para identificar automáticamente el tipo de amenaza cibernética asociada a un evento basado en atributos técnicos de red.

## 2. Objetivo del Modelo
Clasificar eventos entre las siguientes categorías:

- Phishing  
- Malware  
- Ransomware  
- MITM  
- SQL Injection  
- DDoS  

## 3. Dataset Utilizado
- **Nombre:** `amenazas_ciberseguridad_v1.csv`  
- **Registros:** ~3000  
- **Número de clases:** 6  
- **Distribución:** Balanceada  
- **Tipo:** Datos sintéticos simulados de tráfico y eventos de red

## 4. Características Usadas
- timestamp (procesado en componentes temporales)
- source_country
- source_ip (codificada)
- destination_port
- protocol
- packet_size
- device_type
- user_role
- request_type

## 5. Algoritmo Empleado
Modelos candidatos (según experimentación):

- Random Forest  
- Gradient Boosting  
- XGBoost  
- Logistic Regression  
- MLP Classifier  

**Modelo final:**  
> *El mejor modelo se seleccionará según F1-score por clase.*

## 6. Métricas de Rendimiento
(Métricas estimadas — actualizar cuando entrenes el modelo)

- **Accuracy:** ≥ 0.85  
- **F1-Score Macro:** ≥ 0.80  
- **Precision/Recall por clase:** Consistentes y sin clases dominantes  
- **Confusion Matrix:** Distribución aceptable sin sesgos graves  

## 7. Limitaciones
- Basado en datos simulados; puede no capturar patrones avanzados de ataques reales.  
- No analiza payloads ni contenido profundo de paquetes.  
- No detecta amenazas desconocidas (0-day).  
- No funciona en tiempo real sin optimización adicional.

## 8. Riesgos de Uso
- Clasificaciones incorrectas pueden generar falsas alarmas o ignorar amenazas reales.  
- Requiere validación continua si se implementa en entornos reales.  
- No sustituye un SOC o un equipo de ciberseguridad.

## 9. Casos de Uso Adecuados
- Entrenamiento inicial para SOC junior  
- Herramientas de priorización de incidentes  
- Análisis preliminar de eventos  
- Proyectos académicos o de formación

## 10. Casos de Uso NO Recomendados
- Sistemas de detección en tiempo real  
- Infraestructura crítica (gobierno, salud, finanzas) sin validación adicional  
- Reemplazar sistemas SIEM o IDS/IPS

## 11. Versionado del Modelo
- **Versión actual:** v1.0  
- **Formato:** `.pkl`  
- **Almacenamiento:** carpeta `/models/`

## 12. Próximos Pasos
- Reentrenamiento con datos reales del entorno institucional  
- Implementación de pipeline automatizado  
- Integración con herramientas SOC / SIEM  
- Versionado con MLflow
