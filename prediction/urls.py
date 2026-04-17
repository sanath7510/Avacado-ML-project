from django.urls import path
from .views import home
urlpatterns=[path('predict/',home,name='home')]
