from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_index, name='book_index'),
    path('movies/', views.movie_index, name='movie_index'),
]
