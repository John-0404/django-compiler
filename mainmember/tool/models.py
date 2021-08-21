from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Tool(models.Model):
    text = models.CharField(max_length=100,null =True)
    edited_text = models.CharField(max_length=100,null =True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return super().__str__()

    def get_absolute_url(self):
	    return reverse('tool-detail', kwargs={'pk': self.pk})

