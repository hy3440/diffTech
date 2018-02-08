from django.contrib import admin

# Register your models here.

from .models import tags

@admin.register(tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['Tag','Category','TagWiki']