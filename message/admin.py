from django.contrib import admin
from message.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','text','sender','accepter','created_at']
    search_fields = ['id','sender','text','created_at']
    ordering = ['id','created_at','sender']
admin.site.register(Message,MessageAdmin)