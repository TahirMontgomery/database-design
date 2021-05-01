from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getUser, registerUser, loginUser

urlpatterns = [
    path('getuser/', getUser),
    path('registeruser/', registerUser),
    path('loginuser/', loginUser),
]

urlpatterns = format_suffix_patterns(urlpatterns)