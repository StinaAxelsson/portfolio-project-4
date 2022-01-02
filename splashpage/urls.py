from django.urls import path
from . import views
from splashpage.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]