from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
import os
import requests
from .permission import IsAdmin
import boto3
from datetime import datetime


class LogView(APIView):
    # permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['post']

    def post(self, request):
        # Logging Type: INFO, WARN, ERROR, DEBUG
        loggingType = request.data.get('type')
        message = request.data.get('message')

        now = date.now()
        current_date = now.strftime("%Y:%m:%d")
        s3 = boto3.resource('s3')
        s3.Object('cubl-room-booking-log', current_date).put(Body=message)
        return Response()
