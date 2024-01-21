from django.db import models

#описание таблицы user

class User(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=False)
    city = models.CharField(null=True, max_length=64)
    signed = models.BooleanField(default=False)
    chat_id = models.BigIntegerField()
