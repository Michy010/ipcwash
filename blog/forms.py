from django import forms
from .models import Post, Leader

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'file']


class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        fields = ['position', 'name', 'image', 'about_me', 'twitter', 'instagram', 'email',]
