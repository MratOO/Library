from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/<slug:book_slug>/', views.BookDetailView.as_view(),
    name='book_detail'),
    path('<slug:list_slug>/', views.ListView.as_view(), name='book_list'),
    path('register', views.RegisterUser.as_view(), name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)