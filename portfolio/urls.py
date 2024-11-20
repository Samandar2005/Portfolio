from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
