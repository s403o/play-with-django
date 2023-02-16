from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def jan(request):
#   return HttpResponse("learn Python")

# def feb(request):
#   return HttpResponse("learn PostgreSQL")

# def mar(request):
#   return HttpResponse("learn Django")

def monthly_challenges(request, month):
  challenge_text = None
  if month == 'jan':
    challenge_text = "learn Python"
  elif month == 'feb':
    challenge_text = "learn PostgreSQL"
  elif month == 'mar':
    challenge_text = "learn Django"
  else:
    return HttpResponseNotFound("month not supported yet")
  return HttpResponse(challenge_text)