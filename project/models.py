from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    date_added = models.DateField(default=timezone.now)
    image = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
