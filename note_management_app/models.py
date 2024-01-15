from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField( max_length=100, null=True, blank=True)
    body = models.CharField(max_length = 300, null=True, blank=True)