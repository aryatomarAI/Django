from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


# Creating a Class Based views
class CBView(View):
    def get(self,request):
        return HttpResponse("This is an Example of Class based View")

        
