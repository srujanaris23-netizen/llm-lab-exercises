
# Exercise 10: Multi-Node Kubernetes Cluster

## Objective
Deploy multiple applications on a three-node Kubernetes cluster
and demonstrate replica management and service exposure.

## Technologies Used
- Docker
- Minikube
- Kubernetes
- kubectl
- Python
- Flask

## Applications
1. Product Catalog — returns a list of products.
2. Shopping Cart — supports retrieving and adding cart items.

## Kubernetes Configuration
- Cluster: 3 nodes
- Product Catalog replicas: 2
- Shopping Cart replicas: 3
- Services: NodePort
- Pod anti-affinity: distributes replicas of the same application
  across different nodes.

## Files
- product_catalog.py
- shopping_cart.py
- Dockerfile.product
- Dockerfile.shopping
- product-catalog.yaml
- shopping-cart.yaml
- screenshots/

## Verification
The cluster nodes reached Ready status.
Both deployments reached their desired replica counts.
All five application pods reached Running status.
The pods were distributed across all three nodes.
Both Kubernetes Services were created successfully.

## Screenshots
Add screenshots showing:
- Three Ready Kubernetes nodes
- Deployment status
- Pod distribution across nodes
- Services
- Product Catalog API response
- Shopping Cart API response

## Notes
The Shopping Cart application uses in-memory storage.
Cart data is not persistent and is not shared between replicas.

