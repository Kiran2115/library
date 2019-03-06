from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }


    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    # def get_context_data(self, *, object_list=None, **kwargs):
    # #     context = super(BookListView, self).get_context_data(**kwargs)
    # #     context['some_data'] = 'this is just sme data'
    # #     return context
    # # def get_queryset(self):
    #     return Book.objects.filter(title__icontains= 'war')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'

class BookDetailView(generic.DetailView):
    model = Book




