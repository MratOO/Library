from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('/logout/', views.logout_user, name='logout'),
    path('review/<int:pk>', views.CreateReview.as_view(), name='create_review'),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/<slug:book_slug>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<slug:list_slug>/', views.ListView.as_view(), name='book_list'),
    path('<slug:author_slug>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('/login/', views.LoginUser.as_view(), name='login'),
    path('/register/', views.RegisterUser.as_view(), name='registration'),
    path('.search/', views.Search.as_view(), name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)