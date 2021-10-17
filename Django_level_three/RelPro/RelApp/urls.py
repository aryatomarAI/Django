from django.urls import path
from RelApp import views


#Template Tagging
app_name="RelApp"


urlpatterns=[
   path("relative/",views.relative,name="relative"),
   path("other/",views.other,name="other"),

]
