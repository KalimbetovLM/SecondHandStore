from django import forms
from users.models import UserModel
from django.core.mail import send_mail

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username','first_name','last_name','email','password','image']

    def save(self,commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        
        if user.email:
            print(
                "Welcome to our magazin",
                f"Enjoy shooping :)"
            )
        return user
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username','first_name','last_name','email','image']
    


        