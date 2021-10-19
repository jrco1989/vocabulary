from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=CASCADE
    )
    created = models.DateTimeField(
		auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now_add=True
    )
    picture = models.ImageField(
        upload_to = 'user/imagens',
        blank = True,
        null = True
    )

    def __str__(self):
        return self.user.username

class Genre(models.Model):
    name = models.CharField(
        max_length = 50
    )

    user = models.ForeignKey(
        Profile,
        on_delete= models.CASCADE,
        default = ""
    )

    def __str__(self):
        return self.name

class Word(models.Model):
    
    user = models.ForeignKey(
    Profile,
    on_delete= models.CASCADE,
    )
    
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        null=True,
        help_text= 'choice one or more categories'
        )

    title = CharField(
        max_length = 50,
        help_text = 'word searched'
    )
    meaning = CharField(
        max_length= 500,
        help_text='word meaning'
    )
    created = models.DateTimeField(
        auto_now_add= True,
    )
    

    class Meta():
        ordering = ['created']

    def __str__ (self):
        return self.title

class Complement(models.Model):
    
    parent = models.ForeignKey(
        Word,
        on_delete= models.CASCADE,
        default = ""
    )
    user = models.ForeignKey(
        Profile,
        on_delete= models.CASCADE,
        default = ""
        )
    title = CharField(
        max_length = 50,
        help_text = 'word searched'
    )
    meaning = CharField(
        max_length= 500,
        help_text='word meaning'
    )
    created = models.DateTimeField(
        auto_now_add= True,
    )

    def __str__ (self):
        return  self.title
