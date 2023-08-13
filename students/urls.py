from django.urls import path
from . import views

app_name= 'students'

urlpatterns = [
    path('dashboard', views.index, name= 'home'),
    path('election', views.election, name= 'election'),
    path('events', views.events, name= 'events'),
    path('advert', views.advert, name= 'advert'),
    path('issues', views.issues, name= 'issues'),
    path('payment', views.payments, name= 'payment'),
    path('profile', views.users_profiles, name= 'profile'),
    #path('/election', views.election, name= 'election'),
]