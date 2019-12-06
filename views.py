from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
import requests
from .permission import IsAdmin
import boto3
from datetime import datetime
from botocore.exceptions import ClientError
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
        f = open(os.path.join(
            BASE_DIR, 'app/logs/room-booking/log-' + current_date + '.csv'), "a+")
        f.write(message + "\n")
        f.close()

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(
                "log-" + current_date + '.csv', 'cubl-room-booking-log', "log-" + current_date + '.csv')
        except ClientError as e:
            logging.error(e)
            return False
        return True
