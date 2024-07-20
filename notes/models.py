from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=7)
    description = models.TextField()
    course_field = models.CharField(max_length=3)
    prerequisites = models.CharField(max_length=255, blank=True, null=True)
    corequisites = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=2, blank=True, null=True)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.title
    
# class NotesPost(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     description = models.CharField(label="Enter a description", max_length=50)
#     image = models.ImageField(upload_to='user_notes/') 
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__ (self):
#         return f"{self.user.username}'s Note"
        