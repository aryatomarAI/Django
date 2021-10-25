from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.


# Creating a Class Based views
class IndexView(TemplateView):
    template_name="index.html"

    
