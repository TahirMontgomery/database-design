from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from django.db import connection, transaction

@api_view(['POST'])
def getAccount(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM Account where account_id = %s;
            """
            cursor.execute(query, [request.data['account_id']])
            row = cursor.fetchall()

        curAcc = {
                "account_id" : row[0][0],
                "uid" : row[0][1],
                "account_name" : row[0][2],
                "account_type" : row[0][3],
                "balance" :  row[0][4]
        }
        result = AccountSerializer(data=curAcc)
        if result.is_valid():
            return Response(curAcc, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def getAllAccounts(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM Account;
            """
            cursor.execute(query)
            row = cursor.fetchall()

        accounts = []
        for i in row:
            curAcc = {
                    "account_id" : i[0],
                    "uid" : i[1],
                    "account_name" : i[2],
                    "account_type" : i[3],
                    "balance" :  i[4]
            }
            accounts.append(curAcc)

        result = AccountSerializer(data=accounts, many=True)
        if result.is_valid():
            return Response(accounts, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['POST'])
def createAccount(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                query = """
                INSERT INTO Account(uid, account_name, account_type, balance) VALUES(%s, %s, %s, %s);
                """
                cursor.execute(query, [request.data['uid'], request.data['account_name'], request.data['account_type'], request.data['balance']])
                row = cursor.fetchone()
                
                cursor.execute("SELECT * FROM Account WHERE uid=%s", [request.data['uid']])
                row = cursor.fetchall()

            newAccount = {
                        "account_id" : row[0][0],
                        "uid" : row[0][1],
                        "account_name" : row[0][2],
                        "account_type" : row[0][3],
                        "balance" :  row[0][4]
            }
            result = AccountSerializer(data=newAccount)
            if result.is_valid():
                return Response(newAccount, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)