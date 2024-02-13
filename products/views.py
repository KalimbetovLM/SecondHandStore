from django.shortcuts import render,redirect
from products.forms import CreateProductForm,ProductEditForm,ReviewForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product,Reviews,Purchase,Basket
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

class CreateProductView(LoginRequiredMixin,View):

    def get(self,request):
        form = CreateProductForm()        
        context = {
            'form': form
        }
        return render(request,'products/create_product.html',context)
    
    def post(self,request):
        form = CreateProductForm(data=request.POST,
                                 files=request.FILES)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price'],
                image = form.cleaned_data['image'],
                category = form.cleaned_data['category'],
                user = request.user
            )            
            
            messages.success(request,'You have successfully posted your product')
            return render(request,'products/create_product.html',{'form':form})
        else:
            form = CreateProductForm(data=request.POST,
                                     files=request.FILES)
            context = {
                'form': form
            }
            return render(request,'products/create_product.html',context)
        
        

# class CreateProductView(LoginRequiredMixin,View):
    
#     def post(self,request):
#         product_form = CreateProductForm(request.POST)
#         image_form = ProductImageForm(request.POST, request.FILES, prefix='images')
#         if product_form.is_valid() and image_form.is_valid():
#             product = product_form.save(commit=False)
#             product.user = request.user
#             product.save()
#             for f in request.FILES.getlist('images'):
#                 photo = ProductImage(product=product, image=f)
#                 photo.save()
#             context = {
#                 'product_form': product_form,
#                 'image_form': image_form
#             }
#             messages.success(request,"You have successfully posted your product")
#             return render(request,'products/create_product.html',context)
#         else:
#             return render(request,'products/create_product.html', {'product_form': product_form, 'image_form': image_form})
        
#     def get(self,request):
#         product_form = CreateProductForm()
#         image_form = ProductImageForm(prefix='image')
#         return render(request, 'products/create_product.html', {'product_form': product_form, 'image_form': image_form})


class ProductEditView(LoginRequiredMixin,View):
    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        if product.user == request.user:
            form = ProductEditForm(instance=product)
            context = {
                'form': form
            }
            return render(request,'products/product_edit.html',context)
        else:
            messages.warning(request,"You can't edit other user's product")
            
    def patch(self,request,pk):
        product = Product.objects.get(id=pk)
        if product.user == request.user:
            form = ProductEditForm(partial=True,
                                   instance=product,
                                   data=request.POST,
                                   files=request.FILES)
            if form.is_valid():
                form.save()
                messages.info(request,"You hav successfully updated your product")
                return render(request,'products/product_edit.html',{'form':form})
        else:
            messages.warning(request,"You can't edit other user's product")


class ProductListView(View):
    
    def get(self,request):
        product_list = Product.objects.all().order_by('id')
        product_list = product_list.filter(status=Product.Status.Published)
        category = request.GET.get('category','')
        search_query = request.GET.get('q','')
        if search_query:
            product_list = product_list.filter(name__icontains=search_query)
        if category:
            product_list = product_list.filter(category__name=category)
        context = {
            'product_list': product_list,
            'search_query': search_query
        }
        return render(request,'products/products_list.html',context)


class ProductDetailView(View):

    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        reviews = Reviews.objects.filter(product=product)
        review_form = ReviewForm()
        context = {
            'product': product,
            'reviews':reviews,
            'review_form': review_form
        }
        return render(request,'products/product_detail.html',context)
        
    def post(self,request,pk):
        review_form = ReviewForm(data=request.POST)
        product1 = Product.objects.get(id=pk)
        if review_form.is_valid():
            new_review = Reviews.objects.create(
                text = review_form.cleaned_data['text'],
                user = request.user,
                product = product1 
            )
            new_review.save()
            review_form = ReviewForm()
            messages.success(request,"You have successfully added review")
            return redirect(reverse('products:product_detail',kwargs={"pk":product1.id}))
        else:
            review_form = ReviewForm(data=request.POST)
        context = {
            'review_form': review_form
        }

        return render(request,'products/product_detail.html',context)

class ProductDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        if product.user == request.user:
            product.delete()
            messages.info(request,"You hav successfully deleted your product")
            return redirect('products:product_list')
        else:
            messages.warning(request,"You can't delete other users product")


class ProductDeleteConfirmationView(LoginRequiredMixin,View):

    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product
        }
        return render(request,'products/confirmation_delete.html',context)


class MyProductsListView(LoginRequiredMixin,View):

    def get(self,request):
        products = Product.objects.filter(user=request.user)
        context = {
            'products': products
        }
        return render(request,'products/my_products.html',context)
    

class BuyProductView(LoginRequiredMixin,View):

    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        client = request.user
        vendor = product.user
        purchase = Purchase.objects.create(
            vendor = vendor,
            client = client,
            product = product
        )
        Basket.objects.create(
            owner = request.user,
            purchases = purchase
        )
        messages.success(request,"You have successfulyy added this product to your basket")
        return redirect(reverse("products:product_detail",kwargs={'pk':product.id}))


class BasketView(LoginRequiredMixin,View):

    def get(self,request):
        baskets = Basket.objects.all().filter(owner=request.user)
        price_list = []
        for basket in baskets:
            price_list.append(basket.purchases.product.price)
    
        total_price = sum(price_list)
        context = {
            'baskets': baskets,
            "total_price": total_price
        }
        return render(request,'products/basket.html',context)

class RemoveFromBasketView(LoginRequiredMixin,View):
    def get(self,request,pk):
        purchase = Purchase.objects.get(id=pk)
        purchase.delete()
        messages.success(request,"You have successfully removed the product")
        return redirect('products:basket')
    
    

