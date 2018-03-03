from django.contrib import admin

# Register your models here.

from .models import tagPairCompare

@admin.register(tagPairCompare)
class tagPairCompareAdmin(admin.ModelAdmin):
    list_display = ['tag','simiTag','compare']