from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
#views.ListView.as_view(), name='home'

urlpatterns = [
    path('', views.home),
    #path('popular/', views.index, name='popular'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)