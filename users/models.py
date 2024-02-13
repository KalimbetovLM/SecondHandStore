from django.db import models
from django.contrib.auth.models import AbstractUser
from magazin.utilities import set_id

# Create your models here.

class UserModel(AbstractUser):
    id = models.CharField(default=set_id,primary_key=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(default='users/default_user_img.png',null=True,blank=True)



