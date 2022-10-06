from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f'first_name: {self.first_name} last_name: {self.last_name}'