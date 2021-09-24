from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("Title","Author","Contents","Postcategory")
        widgets = {
            "Title":forms.TextInput(attrs={"class":"form-control"}),
            "Author":forms.Select(attrs={"class":"form-control"}),
            "Contents":forms.Textarea(attrs={"class":"form-control"}),
            "Postcategory":forms.Select(attrs={"class":"form-control"}),
        
        }


