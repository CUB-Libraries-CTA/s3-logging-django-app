from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
import requests
from .permission import IsAdmin
from datetime import datetime
import logging
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LogView(APIView):
    http_method_names = ['post']

    def post(self, request):
        # Logging Type: INFO, WARN, ERROR, DEBUG
        loggingType = request.data.get('type')
        message = request.data.get('message')
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        filePath = os.path.join(
            BASE_DIR, 'logs/room-booking/log-' + current_date + '.csv')
        f = open(filePath, "a+")
        f.write(message + "\n")
        f.close()
        return Response({'message': 'success'}, status=status.HTTP_200_OK)
