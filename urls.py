
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fraud/', views.fraud, name='fraud'),
    path('expense/', views.expense, name='expense'),
    path('loan/', views.loan, name='loan'),
]
