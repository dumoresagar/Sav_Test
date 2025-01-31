from django.urls import path
from .views import APICallView

urlpatterns = [
    path('schedule-api/', APICallView.as_view(), name='schedule_api'),
]
