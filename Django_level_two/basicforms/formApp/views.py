from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,"formApp/index.html")


def form_name_view(request):
    form=forms.Form_name()

    if request.method=="POST":
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print("Validation Successful!")
            print("Name:" + form.cleaned_data["name"])
            print("Email:" + form.cleaned_data["email"])
            print("Text:" + form.cleaned_data["text"])

    return render(request,"formApp/form_page.html",{'form':form})
