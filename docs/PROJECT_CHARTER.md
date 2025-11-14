# 📄 Project Charter: MOCACI — Modelo de Clasificación de Amenazas Cibernéticas

## 1. Objetivo de Negocio
La institución enfrenta un volumen creciente de amenazas cibernéticas (phishing, ransomware, DDoS, etc.).  
La clasificación manual de incidentes consume tiempo, depende de la experiencia del analista y aumenta la probabilidad de errores, retrasando la respuesta ante ataques reales.

**Objetivo:**  
Automatizar la clasificación de amenazas para mejorar la eficiencia operativa, reducir el tiempo de análisis y fortalecer la postura de ciberseguridad institucional.

## 2. Objetivo de Data Science
Desarrollar un modelo de machine learning que, a partir de registros de red y atributos asociados, pueda **clasificar automáticamente el tipo de amenaza** dentro de categorías predefinidas como:

- Phishing  
- Ransomware  
- Malware  
- MITM  
- SQL Injection  
- DDoS  

**Pregunta técnica principal:**  
> “Dado un registro de actividad, ¿qué tipo de amenaza representa?”
La amenaza es que dependemos del equipo técnico para identificar manualmente patrones anómalos en 
grandes volúmenes de registros y los tiempos de respuesta son muy altos.

## 3. Alcance

### ✔ Incluye
- Limpieza y preparación del dataset `amenazas_ciberseguridad_v1.csv`
- EDA (análisis exploratorio)
- Feature engineering
- Entrenamiento de modelos de clasificación
- Evaluación con métricas estándar (Accuracy, F1-Score)
- Exportación del modelo final en `.pkl`
- Mockup del MVP
- Documentación técnica

### ❌ No incluye
- Integración del modelo con SIEM o firewalls
- Plataforma final en producción
- Procesamiento en tiempo real
- Automatización de pipelines
- Seguimiento continuo del modelo (MLOps)

## 4. Stakeholders
- **Product Owner:** Timoteo Palacios  
- **Data Scientists / Developers:**  
  - Henry Ramírez  
  - Juan Laug

- **Usuarios Finales:**  
  - Equipo de ciberseguridad  
  - Analistas SOC/NOC  
  - Equipo de respuesta a incidentes  
  - Administradores de red  

## 5. Métricas de Éxito

### Técnicas
- Accuracy ≥ **85%**  
- F1-Score ≥ **0.80** por clase  
- Curva ROC/AUC satisfactoria

### De Negocio
- Reducción del tiempo de clasificación de incidentes  
  **de 20–30 min → < 5 min**
- Disminución de falsos positivos
- Priorización más rápida de amenazas críticas
- Aumento esperado de eficiencia operativa (+20%)

## 6. Timeline
| Hito | Fecha |
|------|--------|
| Inicio del proyecto | 2025-11-10 |
| Entrega MVP (8 semanas) | 2026-01-26 |
| Entrega Final | 2026-06-26 |
