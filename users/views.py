from django.shortcuts import render,redirect
from django.views import View
from users.forms import UserRegisterForm, LoginForm, ProfileUpdateForm  
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserRegisterView(View):
    def get(self,request):
        form = UserRegisterForm()
        context = {
            "form": form
        }
        return render(request,'auth/user_register.html',context)
    
    def post(self,request):
        form = UserRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            form = UserRegisterForm(data=request.POST,files=request.FILES)
            context = {
                'form': form
            }
        return render(request,'auth/user_register.html',context)


class LoginView(View):

    def get(self,request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request,'auth/login.html',context)
    
    def post(self,request):
        form = LoginForm(data=request.POST)
        user = request.user
        if form.is_valid(): 
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"You have successfully logged in")
                return redirect("products:product_list")
            else:
                return HttpResponse("Please,enter correct username or password")
        else:
            return render(request,'auth/login.html',{"form":form})

class LogOut(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.info(request,'You have successfully logged out')
        return redirect('users:login')
    

class ProfileUpdateView(LoginRequiredMixin,View):
    
    def get(self,request):
        form = ProfileUpdateForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request,'auth/profile_update.html',context)
    
    def post(self,request):
        form = ProfileUpdateForm(instance=request.user,
                                 data=request.POST,
                                 files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"You have successfully updated your profile")
            return redirect('users:profile_update')
            
        return render(request,'auth/profile_update.html',{'form':form})
        
