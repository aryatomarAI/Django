from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic
# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by("date")
    date_dict={"access_records":webpages_list}
    my_dict={'insert_me':"In this blog we will see how Django makes everthing simple for us just by few commands. In this blog we are using Static files concept of Django"}
    return render(request,'first_app/index1.html',context=date_dict)
