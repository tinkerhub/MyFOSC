from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	comment = models.CharField(max_length=100)
	email = models.EmailField()
#website = models.URLField()