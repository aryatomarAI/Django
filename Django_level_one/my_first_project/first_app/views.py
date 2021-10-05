from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict={'insert_me':"In this blog we will see how Django makes everthing simple for us just by few commands. In this blog we are using Static files concept of Django"}
    return render(request,'first_app/index.html',context=my_dict)
