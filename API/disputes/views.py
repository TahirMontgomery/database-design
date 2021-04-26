from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Dispute
from .serializers import DisputeSerializer
from django.db import connection, transaction

@api_view(['GET'])
def getAllDisputes(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM Disputes;
            """
            cursor.execute(query)
            row = cursor.fetchall()

        disputes = []
        for i in row:
            cur = {
                    "tid" : i[0],
                    "status" : i[1],
                    "user_reason" : i[2],
                    "admin_comments" : i[3]
            }
            disputes.append(cur)

        result = DisputeSerializer(data=disputes, many=True)
        if result.is_valid():
            return Response(disputes, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def makeDispute(request):
    if request.method == 'POST':
        serializer = DisputeSerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                query = """
                UPDATE Transactions SET status = "Disputed" where tid = %s;
                """
                cursor.execute(query, [request.data['tid']])

                query = """
                INSERT INTO Disputes(tid, status, user_reason, admin_comments) VALUES(%s, %s, %s, %s);
                """
                cursor.execute(query, [request.data['tid'], request.data['status'], request.data['user_reason'], request.data['admin_comments']])
                row = cursor.fetchone()
            
                cursor.execute("SELECT * from Disputes WHERE tid =%s AND status=%s;", [request.data['tid'], request.data['status']])
                row = cursor.fetchall()

            newDispute = {
                "tid" : row[0][0],
                "status" : row[0][1],
                "user_reason" : row[0][2],
                "admin_comments" : row[0][3]
            }
            result = DisputeSerializer(data=newDispute)
            if result.is_valid():
                return Response(newDispute, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUserDisputes(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = """
            select d.tid, d.status, d.user_reason, d.admin_comments from Disputes as d, Transactions as t where uid = %s AND d.tid = t.tid;
            """
            cursor.execute(query, [request.data['uid']])
            row = cursor.fetchall()

        disputes = []
        for i in row:
            cur = {
                    "tid" : i[0],
                    "status" : i[1],
                    "user_reason" : i[2],
                    "admin_comments" : i[3]
            }
            disputes.append(cur)

        result = DisputeSerializer(data=disputes, many=True)
        if result.is_valid():
            return Response(disputes, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def getAccountDisputes(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            query = """
            select d.tid, d.status, d.user_reason, d.admin_comments from Disputes as d, Transactions as t where uid = %s AND account_id =%s AND d.tid = t.tid;
            """
            cursor.execute(query, [request.data['uid'], request.data['account_id']])
            row = cursor.fetchall()

        disputes = []
        for i in row:
            cur = {
                    "tid" : i[0],
                    "status" : i[1],
                    "user_reason" : i[2],
                    "admin_comments" : i[3]
            }
            disputes.append(cur)

        result = DisputeSerializer(data=disputes, many=True)
        if result.is_valid():
            return Response(disputes, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def reviewDispute(request):
    if request.method == 'POST':
        serializer = DisputeSerializer(data=request.data)
        if serializer.is_valid():
            with connection.cursor() as cursor:
                query = """
                Update Transactions Set t.status = "Complete" FROM Disputes as d, Transactions as t WHERE t.tid = %s AND d.tid = %s AND d.status = "Rejected"
                """
                cursor.execute(query, [request.data['tid'], request.data['tid']])
            
                cursor.execute("SELECT * from Disputes WHERE tid =%s;", [request.data['tid']])
                row = cursor.fetchall()

            newDispute = {
                "tid" : row[0][0],
                "status" : row[0][1],
                "user_reason" : row[0][2],
                "admin_comments" : row[0][3]
            }

            result = DisputeSerializer(data=newDispute)
            if result.is_valid():
                return Response(newDispute, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)