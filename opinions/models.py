from django.db import models
from django.contrib.auth.models import User
from posts.models import Like
class Professor(models.Model):# I create a model to represent the professor
    name = models.CharField(max_length=100, unique=True)  #information displayed are the name of the professor and the date this "thread" was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name #returns the professor's name


class ProfessorPost(models.Model): #I created this model to present the professors' posts
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post about {self.professor.name} at {self.created_at}" #returns the professors name and created at date
    
    def like_count(self):
        return self.likes.count() #it returns the number of likes 'hearbeats'
    
class OpinionLike(models.Model): # I created this model for the likes 'hearbeats'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ProfessorPost, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post') #here I ensure that each user can only like a post once
