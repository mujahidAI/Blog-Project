import email
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title', 'text', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tweet text', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Optional detailed content', 'rows': 4}),
        }
 

class UserRegistrationForm(UserCreationForm):
    # add fields that you want to add in the form(these are extras done by the user )
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
