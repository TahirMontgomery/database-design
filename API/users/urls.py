from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getUser, registerUser

urlpatterns = [
    path('getuser/', getUser),
    path('registeruser/', registerUser),
]

urlpatterns = format_suffix_patterns(urlpatterns)