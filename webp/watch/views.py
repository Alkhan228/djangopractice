from django.shortcuts import render


def main_page(request):
    return render(request, 'watch/index.html')


def about_page(request):
    return render(request, 'watch/about.html')
# Create your views here.
