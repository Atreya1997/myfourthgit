from django.urls import path
from app1.views import *
app_name='Something'

urlpatterns=[
    path('Atreya/',Atreya,name='Atreya'),
]