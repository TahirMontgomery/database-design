from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    uid = models.IntegerField(primary_key = True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    role = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'User'