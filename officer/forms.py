from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
import django_filters
from officer.models import User, Division, Department, Position, MemberProfile, Success


#******************* 👍 Operations TARGET MEMBER  *************************#


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user







class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100, help_text='Email')
    username = forms.CharField(
        required=True, max_length=100, help_text='username')
    title = forms.CharField(required=True, max_length=100, help_text='ยศ คำนำหน้า')
    first_name = forms.CharField(required=True, max_length=100, help_text='ชื่อจริง')
    last_name = forms.CharField(required=True, max_length=100, help_text='นามสกุล')
    nick_name = forms.CharField(required=True, max_length=100, help_text='ชื่อเล่น')
    phone = forms.CharField(required=True, max_length=100, help_text='เบอร์โทร')
    # birth_date = forms.DateTimeField(required=True, help_text='วัน เดือน ปีเกิด')
    # profile_picture = forms.IntegerField(help_text = 'รูปภาพโปรไฟล์')

    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)

    error_messages = {
        'password_mismatch': _('รหัสผ่านที่กรอกไม่เหมือนกัน'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_(
            "รหัสผ่านต้องยาวกว่า 8 ตัวอักษร ประกอบด้วยประเภทตามนี้ A,a,1,@#$!"),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("ใส่รหัสผ่านเดิมอีกครั้ง"),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'title',
            'first_name',
            'last_name',
            'nick_name',
            'phone',
            # 'birth_date',
            # 'profile_picture',
        )

    def save(self, commit=True, max_length=100, help_text='Last Name'):
        user = super(UserRegister, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#******************* 👍 Operations  *************************#


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = MemberProfile
        fields = (
            'title',
            'first_name',
            'last_name',
            'nick_name',
            'phone',
        )
