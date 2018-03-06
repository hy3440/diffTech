from django.contrib import admin

# Register your models here.

from .models import tagpaircompare

@admin.register(tagpaircompare)
class tagPairCompareAdmin(admin.ModelAdmin):
    list_display = ['tag','simitag','compare']