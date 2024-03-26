from rest_framework import serializers 
from .models import *

 
class PostSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post 
        fields = '__all__' 
           
class CandidateSerializer(serializers.ModelSerializer): 
    post = PostSerializer() 
    class Meta: 
        model = Candidate 
        fields = '__all__'
            
           