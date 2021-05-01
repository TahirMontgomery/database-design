from rest_framework import serializers
from .models import Transaction, ReturnTransaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ReturnTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnTransaction
        fields = '__all__'