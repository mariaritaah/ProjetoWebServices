from django.shortcuts import render


def all_news(request):
    return render(request, 'index.html')
