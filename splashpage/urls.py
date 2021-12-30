from django.urls import path

from splashpage.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]