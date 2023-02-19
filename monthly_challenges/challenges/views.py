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
    "dec": None,
}
# Create your views here.

# def jan(request):
#   return HttpResponse("learn Python")

# def feb(request):
#   return HttpResponse("learn PostgreSQL")

# def mar(request):
#   return HttpResponse("learn Django")


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = """
    #   <ul>
    #     <li><a href="/challenges/jan">Jan</a></li>
    #   </ul>
    # """
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
          "month": month + " Challenge",
          "text": challenge_text
        })
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
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/jan
    return HttpResponseRedirect(redirect_path)
