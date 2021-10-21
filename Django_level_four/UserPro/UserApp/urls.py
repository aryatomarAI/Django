from django.urls import path
from UserApp import views

#template tagging
app_name="UserApp"

urlpatterns = [
  path("register/",views.register,name="registration")
]
