from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pic = models.ForeignKey('auth.User', on_delete=models.CASCADE)