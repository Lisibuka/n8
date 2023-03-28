from django import forms
from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           # как должна быть реализована графа автор? выбирать можно или напечатать
           'author',
           'categories',
           'title',
           'text',
       ]
