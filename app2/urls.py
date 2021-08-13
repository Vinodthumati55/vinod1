from django.urls import path
from app2.views import *
app_name='vinod'
urlpatterns=[
    path('vinod/',vinod,name='vinod')
]