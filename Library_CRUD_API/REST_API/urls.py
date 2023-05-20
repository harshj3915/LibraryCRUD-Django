from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList),
    path('books/<int:book_Id>/', views.BookDetail),
]
