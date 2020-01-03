import boto3
from botocore.exceptions import ClientError
from rest_framework.response import Response
import os
from datetime import datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now = datetime.now()
s3_client = boto3.client('s3')
current_date = now.strftime("%Y-%m-%d")
filePath = os.path.join(
    BASE_DIR, 'logs/room-booking/log-' + current_date + '.csv')
try:
    response = s3_client.upload_file(
        filePath, 'cubl-log', "room-booking/" + current_date + '.csv')
    os.remove(filePath)
except ClientError as e:
    logging.error(e)
