from django.urls import path 
from . import views 

urlpatterns = [
    # path('books/', views.books) 
    # use class based view
    path('books/', views.BookList.as_view()),
]