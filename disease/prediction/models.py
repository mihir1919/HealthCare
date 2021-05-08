from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

# class /

# class Symptoms(models.Model):
#     id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Person(models.Model):
    name=models.CharField(max_length=200)
    regdate=models.DateTimeField(default=timezone.now)
    dob=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.regdate=timezone.now()
        self.save()

    def __str__(self):
        return self.name

