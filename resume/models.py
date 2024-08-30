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
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    github_path = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)
    site_path = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title