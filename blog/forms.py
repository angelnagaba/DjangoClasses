from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    #title = forms.CharField(label = "email", widget = forms.TextInput(attrs={'class':'form-control'}),required = True)

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
