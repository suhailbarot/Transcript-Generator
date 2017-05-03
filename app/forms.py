from django import forms
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator, URLValidator
from django.contrib.auth.models import User
from django.utils.html import mark_safe




attrs_dict = {'class': 'required'}

class LoginForm(forms.Form):
    """
    Login form for all
    """
    email = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict, maxlength=75)), label=u'Username:')
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label=u'Password:')

    def clean(self):
        """
        Check if user pass combination is correct

        :return:
        """
        if 'email' in self.cleaned_data and 'password' in self.cleaned_data:
            if not authenticate(username=self.cleaned_data['email'], password=self.cleaned_data['password']):
                raise forms.ValidationError(u'The user-password combination is incorrect')
        return self.cleaned_data

    def save(self):
        return authenticate(username=self.cleaned_data['email'], password=self.cleaned_data['password'])