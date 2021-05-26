from django.db import models
from PIL import Image
# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import PersonManager
from tinymce.models import HTMLField  #add

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from own_info import settings


class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone'),max_length=10, null=True)


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    objects = PersonManager()
    
    def __str__(self):
        return self.phone



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



        # super(ModelName, self).save()
        # profile_picture = Image.open(self.photo)
        # (width, height) = profile_picture.size
        # size = ( 100, 100)
        # profile_picture = profile_picture.resize(size, Image.ANTIALIAS)
        # image.save(self.photo.path)


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
        
class Member(models.Model):
    title = models.ForeignKey(Rank, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='picProfile', blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    location = models.ForeignKey(Department, on_delete=models.CASCADE)
    article_published = models.DateTimeField('date published' , default=datetime.now)
    member_content = HTMLField()
    member_slug = models.SlugField()
    

    def __str__(self):
        return self.first_name




class Article(models.Model):
    
    article_title = models.CharField(max_length=200)
    article_published = models.DateTimeField('date published' , default=datetime.now)
    article_image = models.ImageField(upload_to='images/', blank=True, null=True)
    article_content = HTMLField()
    article_slug = models.SlugField()
    
    def __str__(self):
	    return self.article_title
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
