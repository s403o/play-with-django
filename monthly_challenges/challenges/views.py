from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
  return HttpResponse("learn Python")

def feb(request):
  return HttpResponse("learn PostgreSQL")

def mar(request):
  return HttpResponse("learn Django")