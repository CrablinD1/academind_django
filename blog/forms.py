from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your email',
            'text': 'Your comment'
        }


class NewPostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        exclude = ['date', 'slug']