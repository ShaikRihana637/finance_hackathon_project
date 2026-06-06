
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def fraud(request):
    return render(request, 'fraud.html')

def expense(request):
    return render(request, 'expense.html')

def loan(request):
    return render(request, 'loan.html')
