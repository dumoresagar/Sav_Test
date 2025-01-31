from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
from .task_scheduler import make_api_call
import datetime

def schedule_api_calls(timestamps):
    scheduler = BackgroundScheduler()

    for timestamp in timestamps:
        timestamp_time = datetime.strptime(timestamp, '%H:%M:%S').time()
        current_time = now().replace(hour=timestamp_time.hour, minute=timestamp_time.minute, second=timestamp_time.second, microsecond=0)
        scheduler.add_job(make_api_call, 'date', run_date=current_time, args=[timestamp])

    scheduler.start()
