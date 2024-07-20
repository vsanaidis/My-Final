from django.db import models
from django.contrib.auth.models import User
from posts.models import Like
class Professor(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProfessorPost(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post about {self.professor.name} at {self.created_at}"
    
    def like_count(self):
        return self.likes.count()
    
class OpinionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ProfessorPost, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
