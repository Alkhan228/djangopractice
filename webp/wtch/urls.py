from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('about/', about_page, name='about'),
    path('news/', news_page, name='news')
]
