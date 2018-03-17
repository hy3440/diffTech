from django.db import models

# Create your models here.
class tagpaircompare(models.Model):
    tag = models.CharField(max_length = 35)
    simitag = models.CharField(max_length = 35)
    compare = models.CharField(max_length = 500) #max length of compare sentence ['usability','1','1','learnability','2','3'] etc.
        
class relation(models.Model):
	tag = models.CharField(max_length = 35)
	simitag = models.CharField(max_length = 35)
	quality = models.CharField(max_length = 70)
	example_id = models.CharField(max_length = 9)
	example = models.CharField(max_length = 400)


class tagpair(models.Model):
	tag = models.CharField(max_length = 35)
	simitag = models.CharField(max_length = 35)   
    
"""class id_postidtypes(models.Model):
    postid = models.CharField(max_length = 2)
    postidtype = models
    .CharField(max_length = 2)"""