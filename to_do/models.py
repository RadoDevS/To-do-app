from django.db import models
from django.db.models.fields import BooleanField, DateField
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    date = DateField(auto_now_add=True)
    test = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
