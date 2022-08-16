from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='home'),
    path('<slug:slug>/', views.ListView.as_view(), name='book_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)