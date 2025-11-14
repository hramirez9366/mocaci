# 📚 Data Dictionary — MOCACI

Este documento describe cada una de las columnas del dataset `amenazas_ciberseguridad_v1.csv`.

## 🗂 Información General del Dataset
- **Registros:** ~3000  
- **Período simulado:** 2019–2024  
- **Institución:** 700 empleados, 1000 dispositivos  
- **Origen de datos:** Simulación basada en eventos de red internos y externos  
- **Objetivo:** Clasificación de amenazas cibernéticas

## 🧾 Diccionario de Campos

### 1. timestamp
- **Tipo:** datetime  
- **Descripción:** Fecha y hora del evento detectado.  
- **Ejemplo:** `2024-03-01 14:32:10`

### 2. source_ip
- **Tipo:** string  
- **Descripción:** Dirección IP pública externa que generó la solicitud/evento.  
- **Ejemplo:** `185.32.145.90`

### 3. destination_ip
- **Tipo:** string  
- **Descripción:** Dirección IP interna del sistema institucional objetivo  
- **Ejemplo:** `10.2.45.21`

### 4. source_country
- **Tipo:** string  
- **Descripción:** País de origen asociado a la IP de origen.  
- **Ejemplo:** `Russia`, `Brazil`, `USA`

### 5. destination_port
- **Tipo:** int  
- **Descripción:** Puerto de destino solicitado.  
- **Ejemplo:** `443`, `80`, `22`

### 6. protocol
- **Tipo:** string  
- **Descripción:** Protocolo utilizado en el evento de red.  
- **Valores:** `TCP`, `UDP`, `HTTP`, `HTTPS`

### 7. packet_size
- **Tipo:** int  
- **Descripción:** Tamaño del paquete enviado/recibido (bytes).  
- **Ejemplo:** `850`

### 8. request_type
- **Tipo:** string  
- **Descripción:** Tipo de petición realizada.  
- **Valores:** `GET`, `POST`, `CONNECT`, `PUT`

### 9. device_type
- **Tipo:** string  
- **Descripción:** Dispositivo interno sobre el cual ocurrió el evento.  
- **Valores:** `desktop`, `laptop`, `mobile`, `iot`

### 10. user_role
- **Tipo:** string  
- **Descripción:** Rol del usuario asociado al dispositivo.  
- **Valores:** `administrativo`, `analista`, `tecnico`, `beneficiario`

### 11. threat_type (VARIABLE OBJETIVO)
- **Tipo:** categorical  
- **Descripción:** Tipo de amenaza detectada o clasificada.  
- **Ejemplos de clases:**  
  - `phishing`  
  - `malware`  
  - `ddos`  
  - `sql_injection`  
  - `mitm`  
  - `ransomware`

## ✔ Notas Importantes
- Los datos son **simulados**, no contienen información sensible real.  
- Los campos han sido generados para representar patrones propios de una institución con servicios web públicos.  
