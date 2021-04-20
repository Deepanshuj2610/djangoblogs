from django.db import models
from datetime import date
# Create your models here.
class blog(models.Model):
    headings = models.CharField(max_length=20)
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.headings