
from django.urls import path
from .views import article_list, article_detail  #importing views to handle requests

urlpatterns = [
    path('', article_list),
    path('detail/<int:pk>/', article_detail),   # takes in primary key as arguement
]
