from django.shortcuts import render


def news_home(request):
    return render(request, 'watch/news_home.html')

# Create your views here.
