# Docker, Kubernetes & Testcontainers Demo

This demo showcases the integration of **Docker**, **Kubernetes**, and **Testcontainers** to deploy and test services like NGINX, Redis, and MongoDB with real-time logs and container interactions.

## Project Setup

This project demonstrates deploying pods on Kubernetes, running containerized tests with Testcontainers, and fetching logs dynamically for a more interactive demo experience.

### 🖼️ Demo UI Screenshot

<p align="center">
  <img src="assets/docker-k8s-testcontainers-demo-frontend.jpg" alt="Demo UI Screenshot" width="600"/>
</p>

## Features

- **Deploy NGINX, Redis, and MongoDB** pods on Kubernetes.
- **Run tests** with Testcontainers for Redis, MongoDB, and NGINX.
- **Interactive frontend** to view test results, pod status, and deploy/delete actions.

### 🛠️ Technologies Used

- **Docker**
- **Kubernetes**
- **Testcontainers**
- **FastAPI** (Backend)
- **HTML/JavaScript** (Frontend)

## Running the Project Locally

### Prerequisites

1. **Docker Desktop** installed and running (with Kubernetes enabled).
2. **Python 3.12** or above.
3. **kubectl** configured to work with your local Kubernetes cluster.

### 1. Clone the Repository

```bash
git clone https://github.com/vellankikoti/docker-k8s-testcontainers-demo.git
cd docker-k8s-testcontainers-demo
```

### 2. Install Dependencies

#### Backend (Python)
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend
The frontend is a static HTML file, so no installation is needed.

### 3. Start Docker and Kubernetes

Make sure Docker and Kubernetes are running on your machine. Test with:

```bash
kubectl get pods
```

### 4. Run the Application

1. **Start Backend**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Start Frontend**:
   Open the `index.html` in a browser, or use a local HTTP server to serve it (e.g., `python3 -m http.server`).

### 5. Use the Demo

- Select a deployment (NGINX, Redis, MongoDB) from the dropdown.
- Click on **Deploy**, **Delete**, **Status**, or **Run Test** to interact with the Kubernetes cluster and Testcontainers.
- View the test outputs and pod statuses directly in the frontend.

---

### 🚀 Deployment and Test Logs

Test logs from Redis, MongoDB, and NGINX will appear dynamically as you trigger tests and actions through the interface.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
