from django.contrib import admin

from .models import Author, Book, Genres, Commet

admin.site.register(Book)
admin.site.register(Genres)
admin.site.register(Commet)
admin.site.register(Author)
