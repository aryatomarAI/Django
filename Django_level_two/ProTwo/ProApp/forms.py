from  django import forms
from ProApp.models import User



class New_user_form(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
