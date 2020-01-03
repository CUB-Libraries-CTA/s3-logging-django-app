from django.urls import path
from .views import LogView,UploadView

urlpatterns = [
    path('log', LogView.as_view(), name='log'),
    path('upload', UploadView.as_view(), namg='upload')
]
