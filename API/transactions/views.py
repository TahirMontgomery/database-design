from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Transaction, ReturnTransaction
from .serializers import TransactionSerializer, ReturnTransactionSerializer
from django.db import connection, transaction

@api_view(['GET'])
def getUserTransactions(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM Transactions WHERE uid = %s;
            """
            cursor.execute(query, [request.data['uid']])
            row = cursor.fetchall()

        transList = []
        for i in row:
            curTrans = {
                    "tid" : i[0],
                    "account_id" : i[1],
                    "uid" : i[2],
                    "amount" : i[3],
                    "store_name" : i[4],
                    "status" :  i[5]
            }
            transList.append(curTrans)

        result = TransactionSerializer(data=transList, many=True)
        if result.is_valid():
            return Response(transList, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def getAccountTransactions(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM Transactions WHERE account_id =%s AND uid =%s;
            """
            cursor.execute(query, [request.data['account_id'], request.data['uid']])
            row = cursor.fetchall()

        transList = []
        for i in row:
            curTrans = {
                    "tid" : i[0],
                    "account_id" : i[1],
                    "uid" : i[2],
                    "amount" : i[3],
                    "store_name" : i[4],
                    "status" :  i[5]
            }
            transList.append(curTrans)

        result = TransactionSerializer(data=transList, many=True)
        if result.is_valid():
            return Response(transList, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def createTransaction(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                query = """
                INSERT INTO Transactions(account_id, uid, amount, store_name, status) VALUES(%s, %s, %s, %s, %s);
                """
                cursor.execute(query, [request.data['account_id'], request.data['uid'], request.data['amount'], request.data['store_name'], request.data['status']])
                row = cursor.fetchone()
                
                cursor.execute("SELECT * from Transactions WHERE account_id =%s AND uid=%s", [request.data['account_id'], request.data['uid']])
                row = cursor.fetchall()

            newTrans = {
                    "tid" : row[0][0],
                    "account_id" : row[0][1],
                    "uid" : row[0][2],
                    "amount" : row[0][3],
                    "store_name" : row[0][4],
                    "status" :  row[0][5]
            }
            result = TransactionSerializer(data=newTrans)
            if result.is_valid():
                return Response(newTrans, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)