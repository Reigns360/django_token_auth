from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(Voter)