from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #cascade delete user and their info
    title = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) #automatically set the time 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #order whenever completed