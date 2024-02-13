from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from message.forms import MessageForm
from users.models import UserModel
from message.models import Message
from django.contrib import messages

# Create your views here.

class SendMessageView(LoginRequiredMixin,View):
    def get(self,request,pk):
        message_form = MessageForm()
        accepter = UserModel.objects.get(id=pk)
        context = {
            'accepter': accepter,
            'message_form': message_form
        }
        return render(request,'message/messaging.html',context)
    
    def post(self,request,pk):
        message_form = MessageForm(data=request.POST)
        accepter = UserModel.objects.get(id=pk)
        if message_form.is_valid():
            Message.objects.create(
                sender = request.user,
                accepter = accepter,
                text = message_form.cleaned_data['text']
            )
            messages.success(request,"Message has been sended")
            message_form = MessageForm()
        else:
            message_form = MessageForm(data=request.POST)
        context = {
            'accepter': accepter,
            'message_form': message_form
        }
        return render(request,'message/messaging.html',context)


class AcceptedMessageView(LoginRequiredMixin,View):

    def get(self,request):
        accepted_messages = Message.objects.filter(accepter=request.user)
        # sorted_list = []
        # for message in accepted_messages:
            # sorted_list.append(message.sender)
        # sender = sorted_list.pop()
        # accepted_messages = accepted_messages.filter(sender=sender.username)
        
        context = {
            'accepted_messages': accepted_messages
        }
        return render(request,'message/accepted_messages.html',context)
    
        
class MessageDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        my_message = Message.objects.get(id=pk)
        context = {
            'my_message': my_message
        }   
        return render(request,'message/message_detail.html',context)
    


