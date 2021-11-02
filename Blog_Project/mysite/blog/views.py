from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
# Create your views here.



class AboutView(TemplateView):
    template_name="blog/about.html"


# To see all our Posts
class PostListView(ListView):
    model=MyPost

# The queryset will help us display only the list of things we want to see by filtering them
    def get_queryset(self):
        return MyPost.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
        # Here __lte will show all the post, lte stands for less than equal
        # And -published_date will arrange the post in ascending order according to their timezone

# To see post details
class PostDetailView(DetailView):
    model=MyPost



class CreatePostView(LoginRequiredMixin,CreateView):
    login_url="/login/"
    # This will redirect the page If wrong credentials are filled
    redirect_field_name="blog/post_detail.html"

    form_class=PostForm

    model=MyPost


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url="/login/"
    redirect_field_name="blog/post_detail.html"

    form_class=PostForm
    model=MyPost


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=MyPost
    success_url=reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin,ListView):
    login_url="/login/"
    redirect_field_name="blog/post_list.html"

    model=MyPost


    def get_queryset(self):
        return MyPost.objects.filter(published_date__isnull=True).order_by("created_date")
