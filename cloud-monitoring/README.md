# Cloud Monitoring Setup (Local Demo)

## Overview
This project demonstrates *cloud monitoring and alerting* for a cloud-based application.  
Due to restrictions on using AWS, GCP, or Azure, this demo uses a *simulated application and metrics* to illustrate monitoring, dashboards, and alert setup.

*Deliverable:* Configured alerts and a dashboard showcasing metrics.

---

## Steps Performed

1. *Created a demo application*
   - A simple Python application simulates CPU and memory metrics.
   - Metrics are exposed in Prometheus format (cpu_usage and memory_usage).

2. *Configured Monitoring*
   - Prometheus would collect metrics from the application.
   - Metrics were visualized on a Grafana-style dashboard.
   - CPU and memory usage were tracked over time.

3. *Configured Alerts*
   - Simulated alert rule: CPU > 70% triggers a notification.
   - Memory alerts configured similarly.
   - Alerts would notify users when thresholds are exceeded.

4. *Verified Dashboard*
   - Dashboard panels display simulated CPU and memory usage.
   - Alert rules visible on dashboard panels.


## Tools (Simulated)
- Python (for generating sample metrics)  
- Prometheus (metrics collection)  
- Grafana (dashboard visualization)  
- Docker (for containerized setup, if available)

---

## Author
Aseem Prasad
Task 2: Cloud Monitoring and Alerts
