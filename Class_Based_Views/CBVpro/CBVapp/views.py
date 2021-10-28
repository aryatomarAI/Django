from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.


# Creating a Class Based views
class About(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inject_me"]="Basic Injection!!!"

        return context
