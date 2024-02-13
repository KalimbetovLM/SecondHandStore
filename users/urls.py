from django.urls import path
from users.views import UserRegisterView,LoginView,LogOut,ProfileUpdateView

app_name = 'users'
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile_update/',ProfileUpdateView.as_view(),name='profile_update'),
    path('logout/',LogOut.as_view(),name="logout")
]   


