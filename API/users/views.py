from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.db import connection, transaction


# @api_view(['GET'])
# def getUser(request):
#     if request.method == 'GET':
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

@api_view(['POST'])
def getUser(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM User where uid = %s;
            """
            cursor.execute(query, [request.data['uid']])
            row = cursor.fetchall()

        curUser = {
                    "uid" : row[0][0],
                    "first_name" : row[0][1],
                    "last_name" : row[0][2],
                    "email" : row[0][3],
                    "role" :  row[0][4],
                    "password" : row[0][5]
        }
        result = UserSerializer(data=curUser)
        if result.is_valid():
            return Response(curUser, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                query = """
                INSERT INTO User(first_name,last_name, email, role, password) VALUES(%s, %s, %s, %s, %s);
                """
                cursor.execute(query, [request.data['first_name'], request.data['last_name'], request.data['email'], request.data['role'], request.data['password']])
                row = cursor.fetchone()
                
                cursor.execute("Select * from user where email=%s", [request.data['email']])
                row = cursor.fetchall()

            newUser = {
                        "uid" : row[0][0],
                        "first_name" : row[0][1],
                        "last_name" : row[0][2],
                        "email" : row[0][3],
                        "role" :  row[0][4],
                        "password" : row[0][5]
            }
            result = UserSerializer(data=newUser)
            if result.is_valid():
                return Response(newUser, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM User WHERE email=%s AND password=%s;
            """
            cursor.execute(query, [request.data['email'], request.data['password']])
            row = cursor.fetchone()

        if row:
            loggedInUser = {
                            "uid" : row[0],
                            "first_name" : row[1],
                            "last_name" : row[2],
                            "email" : row[3],
                            "role" :  row[4],
                            "password" : row[5]
            }

            return Response(loggedInUser, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)