from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

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