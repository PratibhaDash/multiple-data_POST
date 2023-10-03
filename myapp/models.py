from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/')
