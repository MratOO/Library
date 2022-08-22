from django.db import models
from django.urls import reverse




class Genres(models.Model):

    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, default='')



    def __str__(self):
        return self.name

class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):

    poster = models.ImageField(upload_to='media', blank=True)
    book_view = models.ImageField(upload_to='media', blank=True)
    book_view1 = models.ImageField(upload_to='media', blank=True)
    book_view2 = models.ImageField(upload_to='media', blank=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, 
        related_name='book', 
        on_delete=models.SET_NULL,
        null=True
    )
    genre = models.ForeignKey(
        Genres, 
        related_name='book', 
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.CharField(max_length=8)
    description = models.TextField()
    slug = models.SlugField(max_length=75, default='')

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug':self.genre.slug,
        'book_slug':self.slug})

    
    def __str__(self):
        return self.name
       
        

class Commet(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    book = models.ForeignKey(Book, related_name='commet', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
  