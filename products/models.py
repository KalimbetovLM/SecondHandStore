from django.db import models
from magazin.utilities import set_id
from users.models import UserModel

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.Published)
    
class BlockedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.Blocked)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):

    class Status(models.TextChoices):
        Published = "PB","Published"
        Blocked = "BK","Blocked"

    id = models.CharField(default=set_id,primary_key=True)
    name = models.CharField(max_length=400)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None,related_name='categories')
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/',default='products/default_product_img.png')
    user  = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user')
    publish_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Published)
    objects = models.Manager()
    published = PublishedManager()
    blocked = BlockedManager()

    class Meta:
        ordering = ['-publish_time']
    
    def __str__(self):
        return self.name

class Reviews(models.Model):
    id = models.CharField(default=set_id,primary_key=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='reviews')
    text = models.CharField(max_length=300)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.id


class Purchase(models.Model):
    id = models.CharField(default=set_id,primary_key=True)
    vendor = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='vendor')
    client = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='client')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Basket(models.Model):
    id = models.CharField(default=set_id,primary_key=True)
    purchases = models.ForeignKey(Purchase,on_delete=models.CASCADE,related_name='purchases')
    owner = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='owner')
    updated_at = models.DateTimeField(auto_now=True)


    
