from django.shortcuts import render
from ProApp.forms import New_user_form
# Create your views here.
def index(request):
    return render(request,"ProApp/index.html")


def users(request):
    form=New_user_form
    if request.method=="POST":
        form =New_user_form(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            raise forms.ValidationError("Invalid Details!!, Please Check Again")

    return render(request,"ProApp/sign_up.html",{"form":form})
