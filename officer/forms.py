from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
import django_filters
from officer.models import User, Division, Department, Position, Member


#******************* 👍 Operations TARGET MEMBER  *************************#
class MyAuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'autofocus': True,
                   'class': 'form-control',
                   'id': 'floatingInput',
                   'placeholder': 'Username ไม่ต้องมี @email.com',
                   'size': 30}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'class': 'form-control',
                   'placeholder': 'password',
                   'id': 'floatingPassword'
                   })
    )


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("phone", "username", "email", "password1", "password2")

    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=10)

    error_messages = {
        'password_mismatch': _('รหัสผ่านไม่ตรงกัน'),
    }
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password'}),
        help_text=_("รหัสผ่านต้องยาวกว่า 8 ตัวอักษร และมีความซับซ้อนมากพอ"),
    )
    password2 = forms.CharField(
        label=_("ยืนยัน password อีกครั้ง"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("ใส่รหัสผ่านซ้ำอีกครั้ง ให้เหมือนครั้งแรก"),
    )

    # class Meta:
    #     model = User
    #     fields = ("phone", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.phone = self.cleaned_data['phone']
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
