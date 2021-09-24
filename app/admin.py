from django.contrib import admin

from app.models import Complement
from app.models import Genre
from app.models import Profile
from app.models import Word


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = (
        'pk', 
        'user', 
        'created', 
        )

    list_display_links = (
        'pk', 
        'user',
    )
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = (
        'pk', 
        'user', 
        'created', 
        )

    list_display_links = (
        'pk', 
        'user',
    )

@admin.register(Complement)
class ComplementAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = (
        'pk', 
        'user', 
        'created', 
        )

    list_display_links = (
        'pk', 
        'user',
    )

admin.site.register(Genre)
