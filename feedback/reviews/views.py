from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Reviewform
# from .models import Review

# Create your views here.


def review(request):
    if request.method == "POST":
        # existing_data = Review.objects.get(pk=1)
        form = Reviewform(request.POST) # instance=existing_data (for update)
        if form.is_valid():
            form.save()
            # review = Review(
            #     name=form.cleaned_data["name"],
            #     review_text=form.cleaned_data["review_text"],
            #     rating=form.cleaned_data["rating"],
            # )
            # review.save()
            # print(form.cleaned_data) # {'name': 'name'}

            return HttpResponseRedirect("/thank_you")
    else:
        form = Reviewform()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
