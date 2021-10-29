from django.urls import path,re_path
from CBVapp import views

app_name="CBVapp"


urlpatterns = [
    path('',views.SchoolListView.as_view(),name="list"),
    path("create/",views.SchoolCreateView.as_view(),name="create"),
    re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name="detail"),

]
