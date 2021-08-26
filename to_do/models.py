from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

# Create your models here.
