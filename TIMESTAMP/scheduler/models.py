from django.db import models

# Create your models here.

class ScheduledAPICall(models.Model):
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.timestamp} - {self.status}"
