from django.urls import path
from . import views
from users import views as userstu

app_name= 'mainapp'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('about/', views.about, name= 'about'),
    path('faq/', views.faq, name= 'faq'),
    path('register/', userstu.register, name= 'register'),
    path('login/', userstu.login, name= 'login'),
]