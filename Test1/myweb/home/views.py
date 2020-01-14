from django.shortcuts import render


def index(request):
    msg = 'My Message Test'
    return render(request, 'home/index.html', {'message': msg})