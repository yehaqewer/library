from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()  # Get all books
    search_query = request.GET.get('search', '')  # Get the search term from the URL
    if search_query:
        # Filter the books based on title or author containing the search query
        books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
    else:
        # If no search term is provided, show all books
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm

# Add Book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

# Edit Book
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

# Delete Book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/confirm_delete.html', {'book': book})

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

