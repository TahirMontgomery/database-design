from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import createAccount, getAccount, getAllAccounts

urlpatterns = [
    path('createaccount/', createAccount),
    path('getaccount/', getAccount),
    path('getallaccounts/', getAllAccounts),
]

urlpatterns = format_suffix_patterns(urlpatterns)