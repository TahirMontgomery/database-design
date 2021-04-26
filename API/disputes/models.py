from django.db import models

class Dispute(models.Model):
    tid = models.AutoField(primary_key=True)
    status = models.TextField()
    user_reason = models.TextField()
    admin_comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'Disputes'