from django.conf import settings
from django.db import models
from django.utils import timezone

class Car(models.Model):
    model = models.CharField(max_length=100)
    img = models.ImageField(upload_to='cars')


    def publish(self):
        self.save()

    def __str__(self):
        return self.model