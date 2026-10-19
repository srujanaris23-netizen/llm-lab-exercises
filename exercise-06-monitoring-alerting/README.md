# Exercise 6: Real-Time Operations Monitoring and Alerting

## Objective
Monitor delivery operations using Python metrics, Prometheus,
Grafana dashboards, alert rules, and automated testing.

## Technology Stack
- Python: generates simulated delivery metrics
- prometheus-client: exposes metrics
- Prometheus: collects and evaluates metrics
- Grafana: visualizes operational metrics
- Docker Compose: runs the monitoring services
- Jenkins: automates the test pipeline
- unittest: validates the metrics endpoint

## Architecture
Delivery Metrics Service -> Prometheus -> Grafana Dashboard
                                      -> Alert Rules

Jenkins -> Install Dependencies -> Run Automated Tests

## Metrics
- total_deliveries
- pending_deliveries
- on_the_way_deliveries
- average_delivery_time

## Alert Rules
- HighPendingDeliveries: pending deliveries remain above 10
  for 15 seconds.
- HighAverageDeliveryTime: average delivery time remains above
  30 seconds for 15 seconds.

## Start the Monitoring Stack
docker compose -f compose.yaml up -d --build

## Check Services
docker compose -f compose.yaml ps

## View Metrics
http://localhost:8000/metrics

## Prometheus
http://localhost:9090

## Grafana
http://localhost:3000

## Run Tests
python -m unittest discover -s tests -v

## Stop the Monitoring Stack
docker compose -f compose.yaml down

## Limitations
The delivery metrics are simulated for educational purposes.
They do not represent real delivery company data. Jenkins
automation must be configured and executed separately before
claiming that the CI pipeline has passed.
