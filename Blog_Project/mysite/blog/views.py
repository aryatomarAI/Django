from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from blog.models import MyPost,Comment
from blog.forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
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


#  For Comment Section


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(MyPost,pk)

    if request.method == "POST":
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()

            return redirect("post_detail",pk=post.pk)
    else:
        form=CommentForm()

    return render(request,"blog/comment_form.html",{"form":form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk)
    comment.approve()
    return redirect("post_detail",pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk)
    post_pk=comment.post.pk

    comment.delete()

    return redirect("post_detail",pk=post_pk)


@login_required
def post_publish(request,pk):
    post=get_object_or_404(MyPost,pk)
    post.publish()

    return redirect("post_detail",pk=pk)
