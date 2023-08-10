from django.urls import path
from . import views

app_name= 'students'

urlpatterns = [
    path('', views.index, name= 'home'),
    path('election', views.election, name= 'election'),
    path('events', views.events, name= 'events'),
    path('advert', views.advert, name= 'advert'),
    path('issues', views.issues, name= 'issues'),
    path('payment', views.payments, name= 'election'),
    path('proflie', views.users_profiles, name= 'profile'),
    #path('/election', views.election, name= 'election'),
]