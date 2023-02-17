from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges = {
  "jan": "learn Python",
  "feb": "learn PostgreSQL",
  "mar": "learn Django",
  "apr": "learn Data structure",
  "may": "learn Ruby",
  "jun": "learn Rails",
  "jul": "learn redis",
  "aug": "learn kafka",
  "sep": "learn git",
  "oct": "learn javascript",
  "nov": "learn system design",
  "dec": "learn algorithms",
}
# Create your views here.

# def jan(request):
#   return HttpResponse("learn Python")

# def feb(request):
#   return HttpResponse("learn PostgreSQL")

# def mar(request):
#   return HttpResponse("learn Django")


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>month not supported yet!</h1>")
    # if month == 'jan':
    #     challenge_text = "learn Python"
    # elif month == 'feb':
    #     challenge_text = "learn PostgreSQL"
    # elif month == 'mar':
    #     challenge_text = "learn Django"
    # else:
        # return HttpResponseNotFound("month not supported yet")
    # return HttpResponse(challenge_text)


def monthly_challenge_by_num(request, month):
  months = list(monthly_challenges.keys())
  if month > len(months):
    return HttpResponseNotFound("<h1>Invalid month!</h1>")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/jan
  return HttpResponseRedirect(redirect_path)
