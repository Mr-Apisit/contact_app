from django.db import models
from PIL import Image
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import PersonManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from own_info import settings


class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone'), max_length=10, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    objects = PersonManager()

    def __str__(self):
        return self.phone


class Division(models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=200, unique=True)
    profile_picture = models.ImageField(upload_to='picsPlace', blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=200, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='picsZone', blank=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Rank (models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.TextField(max_length=15)
    tag_slug = models.SlugField()

    def __str__(self):
        return self.tag_name


class Member(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.ForeignKey(Rank, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, unique=True)
    profile_picture = models.ImageField(
        upload_to='picProfile', blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    location = models.ForeignKey(Department, on_delete=models.CASCADE)
    skill_tag = models.ManyToManyField(Tag)
    about_me = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    members = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.members
    



    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
