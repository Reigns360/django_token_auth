from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from Polls.models import Candidate, Post, Voter
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_candidate(request):
    if request.method=='POST':
        form=CandidateCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password1=form.cleaned_data['password1']
            password2=password1=form.cleaned_data['password2']
            if password1 !=password2:
                messages.warning(request,'Passwords don\'t match!')
                return
            user.password=password1
            user.save()
            candidate=Candidate.objects.create(
                user=user,
                post=form.cleaned_data['post'],
                full_name=form.cleaned_data['full_name']
            )
            login(request,user)
        return redirect('home')
    else:
        form=CandidateCreationForm()
    return render(request,'account/CandidateRegistrationForm.html',{'form':form,'page_title':'Candidate Creation Page'})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form,'page_title':'Login Page'})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_voter(request):
    if request.method=='POST':
        form=VoterCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password1=form.cleaned_data['password1']
            password2=password1=form.cleaned_data['password2']
            if password1 !=password2:
                messages.warning(request,'Passwords don\'t match!')
                return redirect('home')
            user.password=password1
            user.save()
            voter=Voter.objects.create(
                user=user,
                voter_ID=form.cleaned_data['voter_ID']
            )
            login(request,user)
        return redirect('home')
    else:
        form=VoterCreationForm()
    return render(request,'account/VoterRegistrationForm.html',{'form':form,'page_title':'Voter Creation Page'})
 
 
 

