from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1><em>This is my seond project</em></h1>")

def help(request):
    my_dict={
    'help_you':"We are here to help you, please tell us in what manner we can help you!"
    }
    return render(request,'project_app/help.html',context=my_dict)
