from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getUserTransactions, createTransaction, getAccountTransactions, createWithdrawal, createDeposit, getAllTransactions

urlpatterns = [
    path('getusertransactions/', getUserTransactions),
    path('getaccounttransactions/', getAccountTransactions),
    path('createtransaction/', createTransaction),
    path('makewithdrawal/', createWithdrawal),
    path('makedeposit/', createDeposit),
    path('getalltransactions/', getAllTransactions),
]

urlpatterns = format_suffix_patterns(urlpatterns)