from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

class EmailSubscribers(models.Model):
    email = models.TextField(max_length=200, unique=True)

    def __str__(self):
        return self.email
