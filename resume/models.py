from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name