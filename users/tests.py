from django.test import TestCase
from users.models import UserModel
from django.urls import reverse
from django.contrib.auth import get_user

# Create your tests here.    
    

class AuthTestCase(TestCase):

    def test_authentification(self):

        response = self.client.post(
        reverse('users:register'),
        data={
            "username":"test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "email": "test_email@gmail.com",
            "password": "test_password"
        }            
        )
        user = UserModel.objects.get(username="test_username")
        users_count = UserModel.objects.count()
        
        reversed_url = reverse("users:login")

        self.assertEqual(users_count,1)
        self.assertEqual(user.username,"test_username")
        self.assertEqual(user.first_name,"test_first_name")
        self.assertEqual(user.last_name,"test_last_name")
        self.assertEqual(user.email,"test_email@gmail.com")
        self.assertNotEqual(user.password,"test_password")
        self.assertTrue(user.check_password,"test_password")
        self.assertEqual(response.url,reversed_url)

    
    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name":"lazizbek",
                "last_name":"kalimbetov"
            }
        )
        form = response.context['form']
        users_count = UserModel.objects.count()

        self.assertEqual(users_count, 0 )
        self.assertFormError(form,"username","This field is required.")
        self.assertFormError(form,"password","This field is required.")


    def test_invalid_email(self):

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "email": "invalid_email",
                "password": "test_password12345"
            }
        )
        form = response.context["form"]
        users_count = UserModel.objects.count()
        
        self.assertEqual(users_count,0)
        self.assertFormError(form,"email","Enter a valid email address.")

    def test_unique_username(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )

        test_user = self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password54321"
            }
        )
        users_count = UserModel.objects.count()
        form = test_user.context["form"]

        self.assertEqual(users_count,1)
        self.assertFormError(form,"username","A user with that username already exists.")

class LoginTestCase(TestCase):
    
    def create_user(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )

    def test_user_loggid_in(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )
        
        self.client.post(
            reverse("users:login"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)


    def test_login_with_wrong_username(self):
        self.create_user()
        response = self.client.post(
            reverse("users:login"),
            data={
                "username": "not_username",
                "password": "test_password12345"
            }
        )

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)
        self.assertContains(response,"Please,enter correct username or password")
    

    def test_login_with_wrong_password(self):
        self.create_user()

        response = self.client.post(
            reverse("users:login"),
            data={
                "username": "test_username",
                "password": "wrong_password"
            }
        )
        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)
        self.assertContains(response,"Please,enter correct username or password")
    

    def test_logging_out(self):
        self.create_user()
        self.client.post(
            reverse("users:login"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )
        
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get(
            reverse("users:logout")
        )
        user = get_user(self.client)
        reversed_url = reverse("users:login")

        self.assertFalse(user.is_authenticated)
        self.assertEqual(response.url,reversed_url)
    

    def test_updated_credentials(self):
        self.create_user()
        self.client.post(
            reverse("users:login"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )

        response = self.client.post(
            reverse("users:profile_update"),
            data={
                "username": "2_test_username",
            }
        )
        user = get_user(self.client)
        user.refresh_from_db()
        reversed_url = reverse("users:profile_update")

        self.assertEqual(user.username,"2_test_username")
        self.assertEqual(response.url,reversed_url)
        

    
                


        
        
    



