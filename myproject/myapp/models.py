from django.db import models

class Greeting(models.Model):
    message = models.CharField(max_length=255)
