from django.urls import path
from .views import LogView

urlpatterns = [
    path('log', LogView.as_view(), name='log'),
]
