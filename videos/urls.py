from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.video, name='video'),
    path('<int:id>.json/', views.transcription, name='transcription'),
]