from django.shortcuts import render
from .models import Book


def viewbook(request):
    c = Book.objects.filter(category='Web Development')
    m = Book.objects.filter(category='Mobile App')
    b = Book.objects.filter(category='Business')
    it = Book.objects.filter(category='IT Software')
    ma = Book.objects.filter(category='Marketing')
    l = Book.objects.filter(category='Lifestyle')
    a = Book.objects.filter(category='Architecture')
    p = Book.objects.filter(category='Photography')
    mu = Book.objects.filter(category='Music')
    e = Book.objects.filter(category='Ecommerce')

    return render(request, 'books/bookgrid.html',{'c': c, 'm': m, 'b': b, 'it': it, 'ma': ma, 'l': l,
                                                   'a': a, 'p': p, 'mu': mu, 'e': e})

