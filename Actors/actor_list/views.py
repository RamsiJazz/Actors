from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def mammootty(request):
    return render(request, 'mammootty.html')


def mohanlal(request):
    return render(request, 'mohanlal.html')


def dileep(request):
    return render(request, 'dileep.html')


def jayasurya(request):
    return render(request, 'jayasurya.html')


def jayaram(request):
    return render(request, 'jayaram.html')


def sreenivasan(request):
    return render(request, 'sreenivasan.html')
