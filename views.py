from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import json
import requests
from .permission import IsAdmin
import boto3
from botocore.exceptions import ClientError
import os
from datetime import datetime, timedelta
import logging

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

class UploadView(APIView):
    http_metthod_names = ['post']

    def post(self, request):
        s3_client = boto3.client('s3')
        yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        filePath = os.path.join(
            BASE_DIR, 'logs/room-booking/log-' + yesterday_date + '.csv')
        if os.path.isfile(filePath):
            try:
                response = s3_client.upload_file(
                    filePath, 'cubl-log', "room-booking/" + yesterday_date + '.csv')
                os.remove(filePath)
            except ClientError as e:
                logging.error(e)
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        else :
            return Response({'message': 'file is not exits'}, status=status.HTTP_200_OK)



