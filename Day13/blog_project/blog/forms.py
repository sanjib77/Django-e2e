from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class UserRegisterForm(UserCreationForm):
    """Form for user registration with email field."""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Validate that email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your post content here...'
            }),
        }

    def clean_title(self):
        """Validate that title is not empty and has minimum length."""
        title = self.cleaned_data.get('title')
        if len(title.strip()) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title
