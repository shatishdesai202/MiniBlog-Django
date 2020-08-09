from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label='Enter Username', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(
        label='Enter Phone', label_suffix=' ', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    message = forms.CharField(
        label='Enter Message', label_suffix=' ', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label='Enter Email', label_suffix=' ', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = '__all__'


class PostForm(forms.ModelForm):
    name = forms.CharField(
        label='Enter Username', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(
        label='Enter Username', label_suffix=' ', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ['post_by']


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Create Password', label_suffix=' ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password', label_suffix=' ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        label='Enter Username', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        label='Enter Firstname', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label='Enter Lastname', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        label='Enter Email', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Enter Username', label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Enter Password', label_suffix=' ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'
