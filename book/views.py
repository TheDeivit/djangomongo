from django.shortcuts import render, redirect
#from pymongo import MongoClient

from django.core.paginator import Paginator

from .models import Book
from .forms import BookForm
# Create your views here.

def index(request):
    return _listBook(request, BookForm())


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return _listBook(request, form)
        
    redirect('book:index')

def update(request, pk):

    book = Book.objects.get(pk = pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        else:
            return _listBook(request, form)
        
    redirect('book:index')


def _listBook(request, form):
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    
    page_number = request.GET.get('page')
    books_page = paginator.get_page(page_number)

    #ESTAS LINEAS SIRVEN PARA EL DROPDOWN LIST
    """client = MongoClient('localhost', 27017)
    db = client['djangomongo']
    collection = db['book_book']
    dropdown_data = []
    for document in collection.find():
        dropdown_data.append(document['name'])"""

    #print(books_page)

    return render(request, 'book/index.html', {'books':books_page, 'form': form})#, 'dropdown_data': dropdown_data