from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

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
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




# id = request.data['id']
# uid = request.data['uid']
# first_name = request.data['first_name']
# last_name = request.data['last_name']
# email = request.data['email']
# role = request.data['role']
# password = request.data['password']
# user = User(id, uid, first_name, last_name, email, role, password)
# user.save()