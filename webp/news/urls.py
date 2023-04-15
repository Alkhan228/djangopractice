from django.urls import path
from .views import *

urlpatterns = [
    path('news/', news_home, name='news_home'),
]
