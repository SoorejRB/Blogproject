from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Category_name = models.CharField(max_length=50)
    Description = models.TextField()
    
    def __str__(self):
        return self.Category_name

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.OneToOneField(User, on_delete=models.CASCADE)
    Contents = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    Postcategory = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    class Meta:    
        ordering =["-Created_on"]

    def __str__(self):
        return str(self.Author) 

