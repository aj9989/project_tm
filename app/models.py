from django.db import models

# Create your models here.
class Task(models.Model):
    DateTime = models.DateTimeField(auto_now=False, blank=False, default='')
    url = models.SlugField(blank=True)
    def __str__(self):
        return self.url




