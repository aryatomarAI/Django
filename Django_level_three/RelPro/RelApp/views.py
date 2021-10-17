from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"RelApp/index.html")
def other(request):
    return render(request,"RelApp/other.html")
def relative(request):
    return render(request,"RelApp/relative_url_temp.html")
