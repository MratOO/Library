
from django.utils import timezone
from django.db import models
from django.urls import reverse




class Genres(models.Model):

    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, default='')



    def __str__(self):
        return self.name

class Author(models.Model):

    name = models.CharField(max_length=100,blank=True)
    portrait = models.ImageField(upload_to='media', blank=True)
    years = models.CharField(max_length=75,blank=True)
    about = models.TextField(max_length=750,blank=True)
    slug = models.SlugField(max_length=75, default='')

    def __str__(self):
        return self.name 

class Book(models.Model):

    poster = models.ImageField(upload_to='media', blank=True)
    book_view = models.ImageField(upload_to='media', blank=True)
    book_view1 = models.ImageField(upload_to='media', blank=True)
    book_view2 = models.ImageField(upload_to='media', blank=True)
    name = models.CharField(max_length=100)
    read = models.URLField(max_length=1000, blank=True)
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
    description = models.TextField()
    slug = models.SlugField(max_length=75, default='')


    def get_review(self):
        return self.comment.all()    

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug':self.genre.slug,
        'book_slug':self.slug})    
       

class Commet(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book}'

