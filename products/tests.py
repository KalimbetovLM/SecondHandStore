from django.test import TestCase
from products.models import Product,Category
from django.urls import reverse
from users.models import UserModel
from django.contrib.auth import get_user

# Create your tests here.

class ProductTestCase(TestCase):

    def create_user(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )
        self.client.login(username="test_username",password="test_password12345")
        

    def test_no_products(self):
        response = self.client.get(
            reverse("products:product_list")
        )
        self.assertContains(response,"No products found")
    
    def test_posting_products(self):
        Category.objects.create(
            name="category"
        )
        categories_count = Category.objects.count()
        self.assertEqual(categories_count,1)
        
        user = UserModel.objects.create(
            username="test_username"
            
        )
        user.set_password("somepassword12345")
        self.client.login(username="test_username",password="somepassword12345")
        
        category1 = Category.objects.get(name="category")
            
        product = Product.objects.create(
            name="test_name",
            description="test_description",
            price = 100,
            category = category1,
            user = user
        )

        products_count = Product.objects.count()
        self.assertEqual(products_count,1)
        self.assertEqual(product.name,"test_name")

    def test_edited_product(self):
        Category.objects.create(
            name="category"
        )
        
        self.client.post(
            reverse("users:register"),
            data={
                "username": "test_username",
                "password": "test_password12345"
            }
        )
        self.client.login(username="test_username",password="test_password12345")
        category1 = Category.objects.get(name="category")
        user = UserModel.objects.get(username="test_username")
        user.save()

        product = Product.objects.create(
            name="test_name",
            description="test_description",
            price = 100,
            category = category1,
            user = user
        )

        self.client.post(
            reverse("products:product_edit", kwargs={"pk":product.pk}),
            data={
                "name": "edited_name",
            }
        )

        product.refresh_from_db()
        products_count = Product.objects.count()

        self.assertEqual(products_count,1)
        self.assertEqual(product.name,"edited_name")

        