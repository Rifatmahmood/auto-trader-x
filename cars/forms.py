# forms.py
from django.contrib.auth.models import User
from django import forms
from .models import Comment
from django.contrib.auth.forms import UserChangeForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email']
        exclude = ['password']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')