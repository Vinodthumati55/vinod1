from django.urls import path
from app1.views import *
app_name='ravi'
urlpatterns=[
    path('ravi/',ravi,name='ravi')
]