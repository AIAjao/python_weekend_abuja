from django.db import models
from django.utils import timezone


# Create your models here.
class post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank =True, null=True)

def pulish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
    return self.title

