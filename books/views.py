from django.shortcuts import render

def list_books(request):
    books = [
        {"title": "Django 3 Web Development Cookbook Fourth Edition", "author": "Aidas Bendoraitis", "rating": 3250},
        {"title": "Two Scoops of Django 3.x", "author": "Daniel Feldroy", "rating": 1570},
        {"title": "El libro de Django", "author": "Adrian Holovaty", "rating": 1200},
        {"title": "Python Web Development with Django", "author": "Jeff Forcier", "rating": 900},
        {"title": "Django for Professionals", "author": "William S. Vincent", "rating": 2100},
        {"title": "Django for APIs", "author": "William S. Vincent", "rating": 2540},
    ]

    high_rated_books = [book for book in books if book["rating"] > 1500]

    context = {
        "high_rated_books": high_rated_books,
        "all_books": books,
    }

    return render(request, 'list_books.html', context)
