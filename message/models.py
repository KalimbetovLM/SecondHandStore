from django.db import models
from django.contrib.auth.models import AbstractUser
from magazin.utilities import set_id
from users.models import UserModel

# Create your models here.
class Message(models.Model):
    id = models.CharField(default=set_id,primary_key=True)
    accepter = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='accepter')
    sender = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='sender')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
# class Chat(models.Model):
#     id = models.CharField(default=set_id,primary_key=True)
