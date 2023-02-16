from django.urls import path
from . import views

urlpatterns = [
  # path('jan', views.jan),
  # path('feb', views.feb),
  # path('mar', views.mar)
  path("<month>", views.monthly_challenges)
]