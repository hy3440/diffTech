from django.db import models

# Create your models here.
class tags(models.Model):
    Tag = models.CharField(max_length = 50)
    Category = models.CharField(max_length = 50)
    TagWiki = models.TextField()
    
class id_postidtypes(models.Model):
    postid = models.CharField(max_length = 2)
    postidtype = models.CharField(max_length = 2)