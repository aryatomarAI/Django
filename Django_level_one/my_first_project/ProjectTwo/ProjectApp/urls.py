from django.urls import path
from ProjectApp import views
urlpatterns=[
path('',views.help,name="help"),
]
