from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

        
class Contact(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField('Email Address')
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.subject
