from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
import django_filters
from officer.models import User, Division, Department, Position, Member, Rank, Tag, Profile
# from tinymce.models import HTMLField  # add
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
        model = Profile
        fields = ('member',)


class MemberForm(forms.ModelForm):
    helper = FormHelper()
    title = forms.ModelChoiceField(queryset= Rank.objects.all(),  to_field_name="name")
    first_name = forms.CharField()
    last_name = forms.CharField()
    nick_name = forms.CharField()
    phone = forms.CharField(max_length=10)
    profile_picture = forms.ImageField()
    position = forms.ModelChoiceField(queryset= Position.objects.all(),to_field_name="name")
    location = forms.ModelChoiceField(queryset= Department.objects.all(),to_field_name="name")
    skill_tag = forms.ModelMultipleChoiceField(queryset= Tag.objects.all(),widget=forms.CheckboxSelectMultiple,to_field_name="tag_slug")
    about_me = forms.CharField()

    class Meta:
        model = Member
        # field = '__all__'
        fields = (
            'title',
            'first_name',
            'last_name',
            'nick_name',
            'phone',
            'profile_picture',
            'location',
            'position',
            'skill_tag',
            'about_me',
        )
        
        # exclude = ['user']
    
    def clean_skill_tag_field(self):
        return ','.join(self.cleaned_data['skill_tag'])
        
    def __str__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-MemberForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(MemberForm, self).__init__(*args, **kwargs)

   
