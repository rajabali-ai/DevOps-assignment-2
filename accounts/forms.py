

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import uploaded_video


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name', 'email', 'password1', 'password2']



class uploaded_videoForm(forms.ModelForm):
    class Meta:
        model = uploaded_video
        fields = ['title', 'uv', ]


