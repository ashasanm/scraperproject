from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts),
    path('scrap', views.scrapProducts)
]