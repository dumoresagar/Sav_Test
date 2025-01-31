import requests
import logging
from datetime import datetime
from celery import shared_task

logging.basicConfig(
    filename='logs/api_calls.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

@shared_task
def make_api_call(timestamp):
    
    try:
        response = requests.get("https://ifconfig.co")
        if response.status_code == 200:
            logging.info(f"Successfully called API at ifconfig.co for timestamp {timestamp}")
        else:
            logging.error(f"Failed to call API at ifconfig.co for timestamp {timestamp}, status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Error calling API at ifconfig.co for timestamp {timestamp}: {str(e)}")
