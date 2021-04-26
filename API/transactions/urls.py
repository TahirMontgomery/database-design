from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getUserTransactions, createTransaction, getAccountTransactions

urlpatterns = [
    path('getusertransactions/', getUserTransactions),
    path('getaccounttransactions/', getAccountTransactions),
    path('createtransaction/', createTransaction),
]

urlpatterns = format_suffix_patterns(urlpatterns)