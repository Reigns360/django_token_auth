from django.urls import path, include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter 
from .views import PostViewSet, CandidateViewSet

router = DefaultRouter() 
router.register(r'posts', PostViewSet) 
router.register(r'candidates', CandidateViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('api/', include(router.urls)),
    path('vote/<int:cand_id>/<int:post_id>/', views.vote, name='vote'),
    path('candidates/<int:pk>/edit/', candidate_edit, name='candidate_edit'),
    path('candidates/<int:pk>/delete/',candidate_delete, name='candidate_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
