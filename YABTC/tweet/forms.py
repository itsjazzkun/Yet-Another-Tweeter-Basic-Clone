from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):  # Use UserCreationForm for built-in features
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'bg-gray-700 text-gray-300 rounded-full px-4 py-2 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Use password1 and password2 for UserCreationForm

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-gray-700 text-gray-300 rounded-full px-4 py-2 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'bg-gray-700 text-gray-300 rounded-full px-4 py-2 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'bg-gray-700 text-gray-300 rounded-full px-4 py-2 transition duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Confirm Password'
            }),
        }

