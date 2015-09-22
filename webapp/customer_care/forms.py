from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import User

__author__ = 'Otto'


class RegisterForm(ModelForm):
    class Meta:
        model = User
        password1 = forms.CharField(label=_("Password"),
                                    widget=forms.PasswordInput)
        password2 = forms.CharField(label=_("Password confirm"),
                                    widget=forms.PasswordInput)
        fields = ('first_name', 'last_name', 'email', 'password', 'password_confirm')
        widget = forms.PasswordInput


class LoginForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
