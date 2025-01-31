from django.test import TestCase
from django.utils.timezone import now, timedelta
from .models import ScheduledAPICall
# Create your tests here.


class APICallTest(TestCase):
    def test_api_call_creation(self):
        timestamp = now() + timedelta(seconds=10)
        api_call = ScheduledAPICall.objects.create(timestamp=timestamp)
        self.assertEqual(api_call.status, "Pending")
