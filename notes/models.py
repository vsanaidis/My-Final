from django.db import models
from django.db import models
from django.contrib.auth.models import User
# My notes model
class Notes(models.Model):# I initialize the title, description etc. for the notes posts
    title = models.CharField(max_length=7)
    description = models.TextField()
    course_field = models.CharField(max_length=3)
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    corequisites = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=2, blank=True, null=True)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title #returns the title (note's title)
