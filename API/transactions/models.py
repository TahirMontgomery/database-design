from django.db import models

class Transaction(models.Model):
    tid = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    uid = models.IntegerField()
    amount = models.FloatField()
    store_name = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Transactions'

class ReturnTransaction(models.Model):
    tid = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    uid = models.IntegerField()
    amount = models.FloatField()
    store_name = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Transactions'