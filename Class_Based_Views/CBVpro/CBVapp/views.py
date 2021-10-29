from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

# Create your views here.


# Creating a Class Based views
class About(TemplateView):
    template_name="index.html"



class SchoolListView(ListView):
    context_object_name="schools"
    model=models.School


class SchoolDetailView(DetailView):
    context_object_name="school_details"
    model=models.School
    template_name="CBVapp/student_details.html"
