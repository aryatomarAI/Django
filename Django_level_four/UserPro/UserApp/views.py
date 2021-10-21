from django.shortcuts import render
from UserApp.forms import UserProfileForm,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,"UserApp/index.html")


def register(request):
    # If you are not registered yet
    registered=False

   # If you have filled the form
    if request.method == "POST":
       #Get the user form info
        user_form=UserForm(request.POST)
        # get the profile form info
        profile_form=UserProfileForm(request.POST)


      # If the filled information is valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save the info once it is valid
            user=user_form.save()
            # Set the password for the user
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if "profile_pic" in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,"UserApp/registration.html",{
                                                       'user_form':user_form,
                                                       'profile_form':profile_form,
                                                       'registered':registered,
                                                        })




def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active():
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")
        else:
            print("SomeOne tried to login into your account and failed!")
            print("Username: {} and password: {}".format(username,password))

            return HttpResponse("Invalid Login Details Entered")
    else:
        return render(request,"UserApp/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You're logged in, Nice!")
