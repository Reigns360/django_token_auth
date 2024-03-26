from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Voter(models.Model):
    full_name = models.CharField(max_length=100)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
       

class Post(models.Model):
    POST_CHOICES = (
        ("P", "President"),
        ("G", "Governor"),
        ("S", "Senator"),
        ("MP", "Member of Parliament"),
    )
    title = models.CharField(max_length=50, choices=POST_CHOICES)
    
    def __str__(self):
        return self.get_title_display()