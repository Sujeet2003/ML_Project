from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name="home"),
    path('calculate-result/', views.calculate, name="result")
    # path('', views.heart)
]