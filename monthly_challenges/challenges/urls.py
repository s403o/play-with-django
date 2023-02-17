from django.urls import path
from . import views

urlpatterns = [
  # path('jan', views.jan),
  # path('feb', views.feb),
  # path('mar', views.mar)
  # order is matter so check first for int then str
  path("", views.index), # /challenges/
  path("<int:month>", views.monthly_challenge_by_num),
  path("<str:month>", views.monthly_challenge, name="month-challenge")
]