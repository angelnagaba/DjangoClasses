from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    #title = forms.CharField(label = "email", widget = forms.TextInput(attrs={'class':'form-control'}),required = True)

    class Meta:
        model = Post
        fields = ('title', 'text',)