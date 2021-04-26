from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getAllDisputes, makeDispute, getUserDisputes, getAccountDisputes, reviewDispute

urlpatterns = [
    path('getalldisputes/', getAllDisputes),
    path('makedispute/', makeDispute),
    path('getuserdisputes/', getUserDisputes),
    path('getaccountdisputes/', getAccountDisputes),
    path('reviewdisputes/', reviewDispute),
]

urlpatterns = format_suffix_patterns(urlpatterns)