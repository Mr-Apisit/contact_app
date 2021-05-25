from django.db import models
from PIL import Image
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import PersonManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from own_info import settings


class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=100, unique=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = PersonManager()

    def __str__(self):
        return self.email

    def __str__(self):
        return self.username


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


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
    profile_picture = models.ImageField(
        upload_to='picsZone',
        blank=True,
        help_text="Profile Picture",
        verbose_name="Profile Picture"       
        )

    def __str__(self):
        return self.name
    
    def save(self):
        if not self.profile_picture:
            return            

        super(ModelName, self).save()
        profile_picture = Image.open(self.photo)
        (width, height) = profile_picture.size     
        size = ( 100, 100)
        profile_picture = profile_picture.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)


class Position(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class MemberProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='picProfile', blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # def save(self, *args, **kwargs):
    #     instance = super(Photo, self).save(*args, **kwargs)
    #     image = Image.open(instance.photo.path)
    #     image.save(instance.photo.path, quality=20, optimize=True)
    #     return instance

#     def __str__(self):
#         return u'Profile of user: %s' % self.user.username

# @receiver(post_save, sender=User) #add this
# def create_user_profile(sender, instance, created, **kwargs):
# 		if created:
# 			Profile.objects.create(user=instance)

# @receiver(post_save, sender=User) #add this
# def save_user_profile(sender, instance, **kwargs):
# 		instance.profile.save()


class Success(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
