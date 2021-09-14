from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.OneToOneField(User, on_delete=models.CASCADE)
    Contents = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)

    class Meta:    
        ordering =["-Created_on"]

    def __str__(self):
        return self.Author