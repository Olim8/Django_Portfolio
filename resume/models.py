from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    github_path = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)
    site_path = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.title