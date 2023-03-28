from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def review(request):
    if request.method == 'POST':
        entered_name = request.POST['name']
        print(entered_name)
        return HttpResponseRedirect('/thank_you')

    return render(request, 'reviews/review.html')

def thank_you(request):
    return render(request, 'reviews/thank_you.html') 