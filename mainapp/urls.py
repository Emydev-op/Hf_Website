from django.urls import path
from . import views

app_name= 'mainapp'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('about/', views.about, name= 'about'),
    path('faq/', views.faq, name= 'faq'),
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
]