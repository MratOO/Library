from django.contrib import admin

from .models import Book, Genres, Commet

admin.site.register(Book)
admin.site.register(Genres)
admin.site.register(Commet)

