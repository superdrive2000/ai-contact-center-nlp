# 🎧 AI Contact Center – Análisis de Satisfacción con NLP

Sistema de análisis de llamadas de un contact center utilizando Inteligencia Artificial.  
Permite transcribir audios y clasificar el sentimiento del cliente, integrando prácticas modernas de despliegue y monitoreo.

---



##  1. Requisitos del sistema

### 🔹 Funcionales

- Transcribir audios de llamadas automáticamente  
- Analizar sentimiento por intervención  
- Clasificar satisfacción (ej: satisfecho, neutral, insatisfecho)  
- Visualizar resultados en dashboard  

---

### 🔹 No funcionales

- Procesamiento escalable (Kubernetes)  
- Baja latencia en inferencia  
- Monitoreo de desempeño del modelo  
- Trazabilidad de experimentos (GitHub Actions) 
- Procesamiento de streaming de llamadas

##  2. Arquitectura <img width="1012" height="675" alt="arquitectura" src="https://github.com/user-attachments/assets/651cf950-fd83-46f0-a8fb-4c33b74a568e" />


## ⚙️ Instalación local

### 1. Clonar repositorio

```bash
git clone <repo>
cd ai-contact-center
```

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ejecutar API

```bash
python app.py
```

---

## 🧪 Prueba del modelo

```bash
curl.exe -X POST http://localhost:5000/analyze -F "audio=@data/sample_calls/Diana_Acaro.wav"
```

---

## 🐳 Docker

### Build

```bash
docker build -t ai-backend:latest ./inference
```

### Run

```bash
docker run -p 5000:5000 ai-backend
```

---

## 📊 Monitoreo

### Levantar servicios

```bash
docker-compose up --build
```

### Accesos

- Grafana: http://localhost:3000  
- Prometheus: http://localhost:9090  

---

## ☸️ Kubernetes (Minikube)

### Iniciar cluster

```bash
minikube start
```

### Desplegar

```bash
kubectl apply -f k8s/
```

### Exponer servicio

```bash
minikube service ai-backend-service
```

---

## 📡 Kafka (Demo)

### Consumer

```bash
python kafka/consumer.py
```

### Producer

```bash
python kafka/producer.py
```

---

## 📈 Weights & Biases

```bash
docker run -e WANDB_API_KEY=YOUR_KEY ai-training
```

---

## 🔄 CI/CD

Pipeline automático con GitHub Actions:

- Build de imagen Docker  
- Push a Docker Hub  

---

## ⚠️ Notas importantes

- Kafka está implementado como módulo desacoplado (modo demostración)  
- El modelo utiliza un dataset pequeño (enfoque en arquitectura, no precisión)  
- Las imágenes Docker pueden ser pesadas por dependencias de IA  

---
---


