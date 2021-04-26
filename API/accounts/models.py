from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    account_name = models.TextField()
    account_type = models.TextField()
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Account'