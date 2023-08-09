from django.db import models

# Create your models here.
class saveforms(models.Model):
    contactName = models.CharField(max_length = 50)
    contactEmail = models.CharField(max_length = 50)
    contactSubject = models.CharField(max_length = 50)
    contactMessage = models.CharField(max_length = 500)