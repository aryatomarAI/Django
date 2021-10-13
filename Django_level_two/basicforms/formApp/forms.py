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
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

# Function defined for botcatcher
#    def clean_botcatcher(self):
    #    botcatcher=self.cleaned_data["botcatcher"]

    #    if len(botcatcher) > 0:
    #        raise forms.ValidationError("Alert BOT!!!!")

    #    return botcatcher
