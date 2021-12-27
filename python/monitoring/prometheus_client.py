# The objective is to send metrics to Prometheus.
# Prometheus client github : https://github.com/prometheus/client_python
# Pip command : pip install prometheus-client
# Pip page : https://pypi.org/project/prometheus-client/

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


registry = CollectorRegistry()
g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
g.set_to_current_time()
push_to_gateway('localhost:9091', job='batchA', registry=registry)
