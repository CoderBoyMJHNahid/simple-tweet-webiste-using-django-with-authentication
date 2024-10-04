from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image']
        labels = {
            'title': 'Post Title',
            'content': 'Post Description',
            'image': 'Upload an Image',
        }

