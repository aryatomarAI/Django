from django.shortcuts import render
from django.http import HttpResponse
from ProjectApp.models import Userinfo
# Create your views here.
def index(request):
    my_dict={
    "welcome":"Go to/users to see the list of user information!",
    }
    return render(request,"project_app/index.html",context=my_dict)

def user(request):
    users_list=Userinfo.objects.order_by("name")
    users_dict={"users":users_list}
    return render(request,'project_app/user.html',context=users_dict)
