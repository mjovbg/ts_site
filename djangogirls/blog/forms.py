from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    '''
    Inherit from ModelForm.
    In class Meta you tell django which model should be used to create this form (in this case it is Post).
    Define fields you want -- title and text
    '''
    class Meta:
        model = Post
        fields = ('title', 'text')

