from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    voter = models.ForeignKey('Voter', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='votes', blank=True, null=True)
    
    def __str__(self):
        if self.user:
            return str(self.user)
        else:
            return "No User"
   

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

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    voter_ID = models.CharField(max_length=100)
    
    def __str__(self):
        return self.voter_ID    

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='candidates', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    background_info = models.TextField()
    manifesto = models.TextField()
    photo = models.ImageField(upload_to="Candidate/photo")
    votes = models.ManyToManyField(Vote, blank=True, null=True)
    
    def __str__(self):
        return self.full_name

    def __str__(self):
        return f"{self.voter.user.username} voted for {self.candidate.full_name}"
    
    def display_pic(self):
        return self.photo.url if self.photo else '/static/assets/default.png'
    
    def __str__(self):
        return self.full_name

# class Result(models.Model):
#     votes = models.ForeignKey('Vote', on_delete=models.CASCADE)
#     candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)

    # def get_vote_count(self):
    #     return Result.objects.filter(candidate=self).count()

    # def get_vote_percentage(self, total_votes):
    #     if total_votes == 0:
    #         return 0.0
    #     return (self.get_vote_count() / total_votes) * 100
    
    # def __str__(self):
    #     return self.full_name
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    