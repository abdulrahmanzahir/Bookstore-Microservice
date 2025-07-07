# 📚 Bookstore REST API with MongoDB & Kubernetes

![Python](https://img.shields.io/badge/Python-3.8-blue)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-blueviolet)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

This project presents a **containerized bookstore management REST API** built using **Flask** and **MongoDB**, deployed on **Kubernetes**. It features a full **CRUD API** setup with robust service discovery, cloud-native deployment, and persistent storage using StatefulSets.

---

## 🧱 Project Structure

```
📁 BOOKSTORE/
├── app/
│   └── bookstore.py               # Flask + PyMongo CRUD API
├── k8s/
│   ├── bookstore-deploy.yaml     # Flask App Deployment on Kubernetes
│   ├── service-mongodb.yaml      # MongoDB Service Configuration
│   ├── bookstore-statefulset.yaml# MongoDB StatefulSet
│   └── config-map.yaml           # ConfigMap for Environment Variables
├── Dockerfile                    # Containerization for the Python app
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Features

- 🔗 Connects to MongoDB via Kubernetes DNS-based service discovery
- 🧠 Performs full CRUD operations on a "books" collection
- 📦 Containerized using Docker
- ⚙️ Deployed and managed using Kubernetes (Pods, Deployments, Services, ConfigMaps)
- 🔒 Persistent volume via StatefulSet for MongoDB
- ☁️ Cloud-native ready (scalable & portable)

---

## ⚙️ Technologies Used

- **Python 3.8**
- **Flask** & **Flask-PyMongo**
- **MongoDB** (NoSQL Database)
- **Docker**
- **Kubernetes**
- **ConfigMaps** & **Environment Variables**

---

## ▶️ How to Run

### 1. Setup MongoDB on Kubernetes

```bash
kubectl apply -f k8s/bookstore-statefulset.yaml
kubectl apply -f k8s/service-mongodb.yaml
```

### 2. Deploy the Flask API

```bash
kubectl apply -f k8s/bookstore-deploy.yaml
```

### 3. Confirm Everything is Running

```bash
kubectl get pods
kubectl get svc
```

---

## 📬 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | `/Books`         | List all books           |
| GET    | `/Books/<id>`    | Get specific book        |
| POST   | `/Books`         | Add a new book           |
| PUT    | `/Books/<id>`    | Update book by ID        |
| DELETE | `/Books/<id>`    | Delete book by ID        |

---

## 📦 Docker Instructions (Optional)

To build and run locally:

```bash
docker build -t bookstore-api .
docker run -p 5000:5000 --env MONGO_URI=mongodb://localhost:27017/Bookstore bookstore-api
```

---

## ✍️ Author

Developed by **Abdulrahman Zahir**  
Database Systems & Cloud Computing — 2024

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
