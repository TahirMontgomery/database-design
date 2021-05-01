from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    role = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'User'