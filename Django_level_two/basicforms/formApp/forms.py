from django import forms
# Buit-in Bot Cathcher
from django.core import validators


# Custom validators
def check_for_Capital(value):
    if value[0].islower():
        raise forms.ValidationError("First Word Should be in Capitals")



class Form_name(forms.Form):
    name=forms.CharField(validators=[check_for_Capital])
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Please enter your email again:")
    text=forms.CharField(widget=forms.Textarea)

    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data["email"]
        vmail=all_clean_data["verify_email"]

        if vmail != email:
            raise forms.ValidationError("Your Email is not matches")
# Function defined for botcatcher
#    def clean_botcatcher(self):
    #    botcatcher=self.cleaned_data["botcatcher"]

    #    if len(botcatcher) > 0:
    #        raise forms.ValidationError("Alert BOT!!!!")

    #    return botcatcher
