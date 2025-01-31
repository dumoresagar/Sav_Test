import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Timestamps.settings')

app = Celery('api_calTimestampsl_scheduler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
