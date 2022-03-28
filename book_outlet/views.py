from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg


def index(request):
    books = Book.objects.all().order_by("-title")
    books_count = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render( request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": books_count,
        "average_rating": avg_rating
        })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render( request, "book_outlet/book_detai.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
        })
