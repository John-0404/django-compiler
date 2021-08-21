from django.db import models

# Create your models here.

class GetInfor(models.Model):
	namefile = models.CharField(max_length = 255, null = True)
	pathfile = models.CharField(max_length = 255, null = True)
	parameter = models.TextField(null=True)
	Res = models.TextField(null=True)
	#output = models.TextField()

	def __str__(self):
		return self.namefile