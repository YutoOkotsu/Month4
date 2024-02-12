from django.shortcuts import render
from . import models


def book_list(request):
    if request.method == 'GET':
        books = models.Book.objects.all()
        return render(request, 'book.html', {'books': books})
# Create your views here.
