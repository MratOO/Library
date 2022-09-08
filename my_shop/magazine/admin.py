from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Book, Genres, Commet


class CommentInline(admin.TabularInline):
    model = Commet
    extra = 1
    readonly_fields = ('name', 'email')

@admin.register(Genres)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'genre')
    list_display_links = ('name', 'author', 'genre')
    list_filter = ('genre', 'author',)
    search_fields = ('name', 'author__name', 'genre__name')
    inlines = [CommentInline]
    save_on_top = True
    #fields = (('author', 'genre'),)
    fieldsets = (
        (None, {
            'fields' : ('name',)
        }),
        (None, {
            'fields' : (('author', 'genre'),)
        }),
        (None, {
            'fields' : ('poster', 'book_view', 'book_view1', 'book_view2',
            'read', 'description', 'slug',)
        }),

    )

@admin.register(Commet)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book')
    list_filter = ('book',)   

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'years') #'get_image')

    #def get_image(self, obj):
        #return mark_safe(f'<img src={obj.portrait.url} width="50" height="60"')

    #get_image.short_description = 'Изображение'   

