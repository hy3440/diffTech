from django.db import models

# Create your models here.
class tags(models.Model):
    Tag = models.CharField(max_length = 50)
    Category = models.CharField(max_length = 50)
    TagWiki = models.TextField()
    