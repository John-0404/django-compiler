from django.db import models

# Create your models here.

class UploadForm(models.Model):
	title = models.CharField(max_length = 255) 
	file= models.FileField()
	body = models.TextField()

	def __str__(self):
		return self.title