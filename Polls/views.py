from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView
from django.db.models import F, Case, When, Count, Value, ExpressionWrapper, FloatField
from django.db.models.functions import Round
from . models import *
from . forms import *
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CandidateSerializer, PostSerializer

 
class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
    
    
def home(request):
    candidate_from_Polls = Candidate.objects.all()
    return render(request, 'Polls/index.html', {'candidate_from_Polls': candidate_from_Polls})

def vote(request,cand_id,post_id):
    candidate=Candidate.objects.filter(id=cand_id).first()
    post=Post.objects.filter(id=post_id).first()
    voter=Voter.objects.filter(user=request.user).first()
    if candidate.votes.filter(post=post, voter=voter).first():
        messages.success(request,f'You have already voted for the {post.get_title_display()} seat!')
        return redirect('home')
    if candidate.votes.filter(voter=voter, post=post).first() == None:
       candidate.votes.create(voter=voter, post=post)
       messages.success(request,f'You have successfully voted for {candidate.user.username}')
    else:
        messages.success(request,f'You cannot vote for {candidate.user.username} twice!')
    return redirect('home')

def result(request):
    candidates = Candidate.objects.annotate(
        total_votes = Count('votes', distinct=True),
        total_votes_per_post = Count('post__votes', distinct=True)
    ).annotate(
        percentage_votes=ExpressionWrapper(
            Case(
                When(total_votes_per_post__gt=0, then=Round(
                    F('total_votes') * 100.0 / F('total_votes_per_post'), 2)),
                default=Value(0),
                output_field=FloatField(),
            ),
            output_field=FloatField(),
        )
    )
    print(candidates)
    context = {
        'candidates': candidates,
    }

    return render(request, 'Polls/result.html', context) 


def candidate_edit(request, pk):
    candidate = Candidate.objects.get(id=pk)
    if request.method=='POST':
        form=CandidateEditForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.password=password
            user.save()
            
            candidate.user=user
            candidate.post=form.cleaned_data['post'],
            candidate.full_name=form.cleaned_data['full_name']
            candidate.save()
            
            login(request,user)
        return redirect('home')
    else:
        form=CandidateEditForm()
    return render(request, 'Polls\candidate_form.htm', {'form':form})  

def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate.delete()
    return redirect('candidate_list')                   


class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class CandidateViewSet(viewsets.ModelViewSet): 
      queryset = Candidate.objects.all() 
      serializer_class = CandidateSerializer
      authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
      permission_classes = [IsAuthenticated]
      
      def get_queryset(self):
        queryset = Candidate.objects.all()
        full_name = self.request.query_params.get('full_name', None)
        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)
        return queryset
    
        def list(self, request, *args, **kwargs): 
            # Custom list function 
            queryset = self.filter_queryset(self.get_queryset()) 
            serializer = self.get_serializer(queryset, many=True) 
            return Response(serializer.data) 
    
        def retrieve(self, request, *args, **kwargs):
            # Custom retrieve function 
            instance = self.get_object() 
            serializer = self.get_serializer(instance) 
            return Response(serializer.data) 
        
        def create(self, request, *args, **kwargs): 
            # Custom create function 
            serializer = self.get_serializer(data=request.data) 
            serializer.is_valid(raise_exception=True) 
            self.perform_create(serializer) 
            headers = self.get_success_headers(serializer.data) 
            return Response(serializer.data, status=201, headers=headers) 
    
        def update(self, request, *args, **kwargs): 
            # Custom update function
            partial = kwargs.pop('partial', False) 
            instance = self.get_object() 
            serializer = self.get_serializer(instance, data=request.data, partial=partial) 
            serializer.is_valid(raise_exception=True) 
            self.perform_update(serializer) 
            return Response(serializer.data) 
        
        def partial_update(self, request, *args, **kwargs): 
            # Custom partial update function 
            return super().partial_update(request, *args, **kwargs) 
        
        def destroy(self, request, *args, **kwargs): 
            # Custom destroy function 
            instance = self.get_object() 
            self.perform_destroy(instance) 
            return Response(status=204)
            

 



    



