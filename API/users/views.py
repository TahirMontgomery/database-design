from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Lead viewset
# class UserViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ] 
#     serializer_class = UserSerializer

# class RegisterViewset(viewsets.ModelViewSet, request):
#     queryset = User.objects.all()


@api_view(['GET'])
def getUser(request):
    if request.method == 'GET':
        # serializer = UserSerializer(data=request.data)
        queryset = User.objects.all()
        users = UserSerializer(data=queryset)
        if users.is_valid():
            return Response(users.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def registerUser(request):
#     if request.method == 'POST':
#         pass