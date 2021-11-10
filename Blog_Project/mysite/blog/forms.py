from django import forms
from blog.models import MyPost, Comment
from django.forms import ModelForm, Textarea


class PostForm(forms.ModelForm):
    class Meta:
        model=MyPost
        fields=("author","title","text")


        # Widgets
        widgets={'title':forms.Textarea(attrs={"class":"textInputClass",'placeholder':'Enter a Value'}),
                 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent','placeholder':'Enter your blog'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("author","text")

        widgets={"author":forms.TextInput(attrs={"class":'textInputClass'}),
                  "text":forms.Textarea(attrs={'class':'editable medium-editor-textarea','placeholder':'Comment Here'})

                 }
