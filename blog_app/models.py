from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=1000)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # shows the latest post first 
    class Meta:
        ordering = ['-date_created']