# Exercise 2: Deploy Flask on Minikube

## Objective
Deploy a Flask web application to a local Kubernetes cluster using Minikube and kubectl.

## Technologies
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Application endpoints
- `/` — Displays application status.
- `/health` — Returns a health status.

## Kubernetes resources
- Deployment: `flask-app-deployment`
- Service: `flask-app-service`
- Service type: NodePort
- Container port: 15000
- NodePort: 30080

## Files
- `app.py` — Flask application
- `requirements.txt` — Python dependency
- `Dockerfile` — Container image configuration
- `deployment.yaml` — Kubernetes Deployment
- `service.yaml` — Kubernetes Service

## Execution
Follow the repository's Exercise 2 setup instructions to build the image, load it into Minikube, apply the Kubernetes YAML files, and access the application.

## Expected result
The home endpoint returns a JSON message confirming that the Flask application is running.
The health endpoint returns `{"status": "healthy"}`.
