from django.shortcuts import get_object_or_404, render_to_response, RequestContext
from .models import Library, Book
from django.http import HttpResponseRedirect
from django.template import RequestContext


def library_view(request):
    library = list(Library.objects.all().values())
    print library
    return render_to_response('index.html', locals())


def book_view(request,slug):
    library = get_object_or_404(Library, slug=slug)
    books = library.book_set.all()
    library_name = library.library_name
    library_slug = library.slug
    return render_to_response('books.html', locals())

def add_new_book(request,slug):
    library = get_object_or_404(Library, slug=slug)
    library_name = library.library_name
    library_slug = library.slug
    return render_to_response("add_book.html", locals() , context_instance=RequestContext(request))


def submit_book(request,slug):
    if request.method == 'POST':
        library = get_object_or_404(Library, slug=slug)
        library_name = library.library_name
        library_slug = library.slug
        if request.POST['book_name']:
            book = Book(book_name=request.POST['book_name'], library= library)
            book.save()
        else:
            print "Invalid"
        return HttpResponseRedirect('/books/'+library_slug)
    return render_to_response("books.html", locals() , context_instance=RequestContext(request))
