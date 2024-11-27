from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('api/books/', views.BookListCreate.as_view(), name='book_list_create_api'),
    path('api/books/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view(), name='book_retrieve_update_destroy_api'),
]
