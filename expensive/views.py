from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'expensive/index.html')


def AddExpensives(request):
    return render(request, 'expensive/addexpnesive.html')

