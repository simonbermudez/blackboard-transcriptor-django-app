from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("<h1>Welcome to Blackboard Transcriptor</h1>")