from Polls.models import Candidate, Post, Voter, Vote
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CandidateCreationForm(UserChangeForm):
    full_name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}), label='password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), label='Confirm Password')
    post = forms.ModelChoiceField(queryset=Post.objects.all(), empty_label=None)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class VoterCreationForm(UserChangeForm):
    voter_ID = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}), label='password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), label='Confirm Password')
    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']        


        
        
        
        