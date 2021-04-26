from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import createAccount, getAccount

urlpatterns = [
    path('createaccount/', createAccount),
    path('getaccount/', getAccount),
]

urlpatterns = format_suffix_patterns(urlpatterns)