from django.urls import path
from message.views import SendMessageView,AcceptedMessageView, MessageDetailView

app_name = 'message'
urlpatterns = [
    path('<str:pk>/message/',SendMessageView.as_view(),name='send_message'),
    path('accepted/',AcceptedMessageView.as_view(),name='accepted_messages'),
    path('<str:pk>/message_detail/',MessageDetailView.as_view(),name='message_detail')
]
