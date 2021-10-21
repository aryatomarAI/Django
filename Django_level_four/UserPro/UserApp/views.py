from django.shortcuts import render
from UserApp.forms import UserProfileForm,UserForm
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
