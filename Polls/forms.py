from django import forms
from django.contrib.auth.forms import UserChangeForm 
from . models import Candidate, Post, Voter, Vote
from django.contrib.auth.models import User        
        
class CandidateEditForm(UserChangeForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), empty_label=None)
    background_info = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password']        
        
                   