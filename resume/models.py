from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us'

    def __str__(self):
        return f'Message from {self.name}'