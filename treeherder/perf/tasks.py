import newrelic.agent
from celery import task

from treeherder.perf.alerts import generate_new_alerts_in_series
from treeherder.perf.models import PerformanceSignature


@task(name='generate-alerts')
def generate_alerts(signature_id):
    newrelic.agent.add_custom_parameter("signature_id", str(signature_id))
    signature = PerformanceSignature.objects.get(id=signature_id)
    generate_new_alerts_in_series(signature)
