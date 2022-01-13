from django.urls import path
from .views import PM_detail

urlpatterns = [
    path('inbox/', PM_detail.as_view(), name='messages'),
]