from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={
         'text':"This is the example of Template filter",
         'number':100,
    }
    return render(request,"RelApp/index.html",context=context_dict)

def other(request):
    return render(request,"RelApp/other.html")
    
def relative(request):
    return render(request,"RelApp/relative_url_temp.html")
