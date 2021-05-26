from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
import django_filters
from officer.models import User, Division, Department, Position, Member


#******************* 👍 Operations TARGET MEMBER  *************************#


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "phone")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

#******************* 👍 Operations  *************************#


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = (
            'title',
            'first_name',
            'last_name',
            'nick_name',
            'phone',
        )
