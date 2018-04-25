from django.db import models

# Create your models here.
class tagpaircompare(models.Model):
    tag = models.CharField(max_length = 35)
    simitag = models.CharField(max_length = 35)
    compare = models.CharField(max_length = 500) #max length of compare sentence ['usability','1','1','learnability','2','3'] etc.
        
class relation(models.Model):
	tag = models.CharField(max_length = 35)
	simitag = models.CharField(max_length = 35)
	quality = models.CharField(max_length = 1000) #limit 1000 70
	example_id = models.CharField(max_length = 600) #limit 600 9
	example = models.CharField(max_length = 60000) #limit 65535?? 400


class tagpair(models.Model):
	tag = models.CharField(max_length = 35)
	simitag = models.CharField(max_length = 35)   
    
