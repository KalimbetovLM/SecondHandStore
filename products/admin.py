from django.contrib import admin
from products.models import Product,Category, Reviews, Basket, Purchase

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','user_id','price','category','image','publish_time')
    search_fields = ('id','name','description')
    ordering = ['publish_time','price']

admin.site.register(Product,ProductAdmin)

admin.site.register(Category)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','user','product')
    search_fields = ('id','text')
admin.site.register(Reviews,ReviewsAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id','vendor','client','product','created_at')
    search_fields = ('id','product')
    ordering = ['id','created_at']
admin.site.register(Purchase,PurchaseAdmin)

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id','owner','updated_at')
    search_fields = ('id','owner')
    ordering = ['updated_at']
admin.site.register(Basket,BasketAdmin)
    
    


