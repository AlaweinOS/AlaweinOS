Deployment Guide
================

MEZAN V4.1.0 provides multiple deployment options for different environments.

Quick Start
-----------

Docker Compose (Development/Testing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clone repository
   git clone https://github.com/AlaweinOS/AlaweinOS.git
   cd AlaweinOS

   # Start all services (CPU only)
   cd docker
   docker-compose up -d

   # Start with GPU support
   docker-compose --profile gpu up -d

   # Start with Jupyter for demos
   docker-compose --profile dev up -d

   # Check status
   docker-compose ps

   # View logs
   docker-compose logs -f mezan-api

   # Stop all services
   docker-compose down

**Access Points:**

* MEZAN API: http://localhost:8080
* Grafana: http://localhost:3000 (admin/mezan_admin_2025)
* Prometheus: http://localhost:9091
* Jupyter: http://localhost:8888 (token: mezan2025)

Kubernetes (Production)
~~~~~~~~~~~~~~~~~~~~~~~~

Step 1: Create Namespace
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   kubectl apply -f k8s/mezan-deployment.yaml

This creates:

* Namespace: ``mezan``
* ConfigMaps for configuration
* Secrets for sensitive data
* Deployments (API + GPU worker)
* Services (ClusterIP)
* Persistent Volume Claims
* Ingress with TLS
* HorizontalPodAutoscaler
* PodDisruptionBudget

Step 2: Deploy Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   kubectl apply -f k8s/monitoring.yaml

This creates:

* Prometheus deployment
* Grafana deployment
* ServiceAccount + RBAC
* ConfigMaps for provisioning

Step 3: Verify Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Check all pods are running
   kubectl get pods -n mezan -w

   # Check services
   kubectl get svc -n mezan

   # Check ingress
   kubectl get ingress -n mezan

   # View logs
   kubectl logs -n mezan -l app=mezan,component=api -f

Step 4: Update DNS
^^^^^^^^^^^^^^^^^^

Point your domain to the Ingress LoadBalancer IP:

.. code-block:: bash

   kubectl get ingress -n mezan -o wide
   # Update DNS A record: mezan.yourdomain.com → EXTERNAL-IP

Configuration
-------------

Environment Variables (ConfigMap)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   MEZAN_ENV: production
   MEZAN_LOG_LEVEL: INFO
   MEZAN_REDIS_URL: redis://redis:6379/0
   MEZAN_PROMETHEUS_PORT: 9090

Secrets (must be updated)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Update Redis password
   kubectl create secret generic mezan-secrets \\
     --from-literal=redis-password='YOUR_SECURE_PASSWORD' \\
     -n mezan --dry-run=client -o yaml | kubectl apply -f -

   # Update Grafana admin password
   kubectl create secret generic grafana-secret \\
     --from-literal=admin-password='YOUR_SECURE_PASSWORD' \\
     -n mezan --dry-run=client -o yaml | kubectl apply -f -

Monitoring
----------

Access Grafana
~~~~~~~~~~~~~~

.. code-block:: bash

   # Port-forward Grafana
   kubectl port-forward -n mezan svc/grafana 3000:3000

   # Open http://localhost:3000
   # Login: admin / mezan-admin-change-me (UPDATE THIS!)

Dashboards
~~~~~~~~~~

1. **MEZAN Overview**: Pre-loaded with 13 panels

   * Solver execution rate
   * Latency percentiles (P50/P95/P99)
   * GPU utilization
   * Meta-learning metrics
   * System health

Prometheus Queries
~~~~~~~~~~~~~~~~~~

.. code-block:: promql

   # Solver execution rate
   rate(libria_qap_solve_duration_seconds_count[5m])

   # P95 latency
   histogram_quantile(0.95, rate(libria_qap_solve_duration_seconds_bucket[5m]))

   # GPU utilization
   libria_qap_gpu_utilization_percent

Testing Deployment
------------------

Health Checks
~~~~~~~~~~~~~

.. code-block:: bash

   # MEZAN API health
   curl http://localhost:8080/health

   # Prometheus targets
   curl http://localhost:9091/api/v1/targets

   # Redis connection
   redis-cli -h localhost ping

Run Sample Optimization
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Inside mezan-api pod
   kubectl exec -it -n mezan deploy/mezan-api -- python3 << 'EOF'
   from MEZAN.core import OptimizationProblem, ProblemType, OptimizerFactory

   problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={
           "distance_matrix": [[0,10,20],[10,0,15],[20,15,0]],
           "flow_matrix": [[0,5,3],[5,0,2],[3,2,0]]
       }
   )

   factory = OptimizerFactory()
   optimizer = factory.create_optimizer(problem)
   result = optimizer.solve(problem)

   print(f"Status: {result.status}")
   print(f"Solution: {result.solution}")
   EOF

Scaling
-------

Manual Scaling
~~~~~~~~~~~~~~

.. code-block:: bash

   # Scale API pods
   kubectl scale deployment mezan-api -n mezan --replicas=5

   # Scale GPU workers
   kubectl scale deployment mezan-gpu-worker -n mezan --replicas=2

Auto-Scaling (Already Configured)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **HPA**: 3-10 pods based on CPU (70%) and Memory (80%)
* **Scaling Behavior**:

  * Scale up: 100% every 30s (aggressive)
  * Scale down: 50% every 60s (conservative, 5min stabilization)

Monitor Auto-Scaling
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   kubectl get hpa -n mezan -w

Security Hardening
------------------

Update TLS Certificate
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Assuming cert-manager is installed
   kubectl apply -f - <<EOF
   apiVersion: cert-manager.io/v1
   kind: Certificate
   metadata:
     name: mezan-tls
     namespace: mezan
   spec:
     secretName: mezan-tls
     issuerRef:
       name: letsencrypt-prod
       kind: ClusterIssuer
     dnsNames:
       - mezan.yourdomain.com
   EOF

Troubleshooting
---------------

Pods Not Starting
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check pod status
   kubectl describe pod -n mezan <pod-name>

   # Check events
   kubectl get events -n mezan --sort-by='.lastTimestamp'

   # Check logs
   kubectl logs -n mezan <pod-name> --previous

Redis Connection Issues
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Test Redis connectivity
   kubectl exec -it -n mezan deploy/mezan-api -- redis-cli -h redis ping

   # Check Redis logs
   kubectl logs -n mezan sts/redis

GPU Not Detected
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check GPU availability
   kubectl describe node | grep -i gpu

   # Verify NVIDIA device plugin
   kubectl get pods -n kube-system | grep nvidia

   # Check GPU worker logs
   kubectl logs -n mezan deploy/mezan-gpu-worker

Backup & Recovery
-----------------

Backup Persistent Data
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Backup MEZAN data
   kubectl exec -n mezan sts/redis -- redis-cli BGSAVE
   kubectl cp mezan/<redis-pod>:/data/dump.rdb ./backup/redis-$(date +%Y%m%d).rdb

   # Backup Prometheus data
   kubectl exec -n mezan deploy/prometheus -- tar -czf /tmp/prometheus-backup.tar.gz /prometheus
   kubectl cp mezan/<prometheus-pod>:/tmp/prometheus-backup.tar.gz ./backup/

Restore from Backup
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Restore Redis
   kubectl cp ./backup/redis-backup.rdb mezan/<redis-pod>:/data/dump.rdb
   kubectl rollout restart statefulset redis -n mezan

For complete deployment runbook, see: ``DEPLOYMENT_RUNBOOK.md``
