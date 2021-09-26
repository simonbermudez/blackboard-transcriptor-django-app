from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from videos.models import *

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,template_name='index.html',context = {'videos': Video.objects.all()})

def video(request, id):
    return render(request,template_name='video.html',context = {'video': Video.objects.get(id=id)})

def transcription(request, id):
    video = Video.objects.get(id=id)
    return JsonResponse({'title': video.title, 'transcription': video.transcription })