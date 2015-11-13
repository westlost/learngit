from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import Book,Author
from django.views.decorators.csrf import csrf_exempt
#from models import Author,Book

#from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        i = request.POST['delete']
        s = Book.objects.get(ISBN = i)
        if s:
            book = Book.objects.get(ISBN = i)
            book.delete()
    books = Book.objects.all()
    return render_to_response('index.html',{'books':books})

def information(request,i):
    book = Book.objects.get(ISBN = i)
    return render_to_response('information.html',{'book':book})

@csrf_exempt
def addbook(request):
    authors = Author.objects.all()
    if request.method == "POST":
        ID = request.POST['AuthorID']
        
        #ISBN = request.POST['ISBN']
        #Title = request.POST['Title']
        AuthorID = Author.objects.get(AuthorID = ID)
        #Publisher = request.POST['Publisher']
        #PublishDate = request.POST['PublishDate']
        #Price = request.POST['Price']
        Book.objects.create(ISBN = request.POST['ISBN'],
                            Title = request.POST['Title'],
                            AuthorID = Author.objects.get(AuthorID = ID),
                            Publisher = request.POST['Publisher'],
                            PublishDate = request.POST['PublishDate'],
                            Price = request.POST['Price'])
    return render_to_response('addbook.html',{'authors':authors})

def search(request):
    if request.method == 'GET':
        
        if 'name' in request.GET and request.GET['name']:
            name = request.GET['name']
            s = Author.objects.filter(Name = name)
            if s:
                author = Author.objects.get(Name = name)
                books = author.book_set.all()
                return render_to_response('search.html',{'author':author,'books':books})
    return render_to_response('search.html')
@csrf_exempt
def addauthor(request):
    if request.method == "POST":
        Author.objects.create(AuthorID = request.POST['AuthorID'],
                            Name = request.POST['Name'],
                            Age = request.POST['Age'],
                            Country = request.POST['Country'])
    return render_to_response('addauthor.html')
@csrf_exempt
def update(request,i):
    authors = Author.objects.all()
    ISBN = i
    book = Book.objects.get(ISBN = ISBN)
    if request.method == "POST":
        ID = request.POST['AuthorID']
        AuthorID = Author.objects.get(AuthorID = ID)
        book.Title = request.POST['Title']
        book.AuthorID = Author.objects.get(AuthorID = ID)
        book.Publisher = request.POST['Publisher']
        book.PublishDate = request.POST['PublishDate']
        book.Price = request.POST['Price']
        book.save()
    return render_to_response('update.html',{'book':book,'authors':authors})



        
