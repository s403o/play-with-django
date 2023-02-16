from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("month not supported yet!")
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
    return HttpResponseNotFound("Invalid month!")
  redirect_month = months[month - 1]
  return HttpResponseRedirect("/challenges/" + redirect_month)
