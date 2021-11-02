from django.db import models
from django.urls import reverse
# Create your models here.


class MyPost(models.Model):
    # Check if the author is authorised or not
    author =models.ForeignKey("auth.User")

    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    pblication_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


class Comment(models.Model):
    post=models.ForeignKey("blog.POST",related_name="comments")

    author=models.CharField(max_length=200)

    text=models.TextField()

    create_date=models.DateTimeField(default=timezone.now())

    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list")