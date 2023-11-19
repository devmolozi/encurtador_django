from django.urls import path, include
from molozify import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('link/', views.link, name='link'),
    path('<str:link>/', views.redirecionar, name='redirecionar'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
