from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact, Product

class signup(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-user'}))
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class': 'form-password', 'placeholder' : 'Enter Password'}))
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-password', 'placeholder' : 'Re-Enter Password For Confirmation'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-email', 'placeholder' : 'Enter a Valid Email  Eg:- username@domain.com'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-name', 'placeholder' : 'Enter Your First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-name', 'placeholder' : 'Enter Your Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




class contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-title', 'placeholder' : 'Enter Query Title'}),
            'author': forms.TextInput(attrs={'class' : 'form-author', 'value' : '', 'type' : 'hidden', 'id':'user'}),
            'body': forms.Textarea(attrs={'class' : 'form-body', 'placeholder' : 'Enter Query Message', 'rows' : '10'}),
        }