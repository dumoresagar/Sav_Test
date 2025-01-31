from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime
from datetime import datetime
from .models import ScheduledAPICall
from .serializers import APICallSerializer
from .task_scheduler import make_api_call

class APICallView(APIView):
    def post(self, request):
        timestamps = request.data.get("timestamps", "")
        
        if not timestamps:
            return Response({"error": "No timestamps provided"}, status=status.HTTP_400_BAD_REQUEST)

        timestamp_list = timestamps.split(",")
        created_entries = []

        for timestamp in timestamp_list:
            dt = parse_datetime(timestamp.strip())
            if dt is None or dt < datetime.now():
                continue
            
            api_call = ScheduledAPICall.objects.create(timestamp=dt)
            make_api_call.apply_async((api_call.id,), eta=dt)  # Schedule API Call
            created_entries.append(api_call)

        serializer = APICallSerializer(created_entries, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
