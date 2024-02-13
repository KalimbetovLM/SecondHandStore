from django.urls import path
from products.views import CreateProductView,ProductEditView,ProductListView, \
    MyProductsListView,ProductDeleteView,ProductDeleteConfirmationView, \
    BuyProductView, BasketView, ProductDetailView, RemoveFromBasketView

app_name='products'
urlpatterns = [
    path('basket/',BasketView.as_view(),name='basket'),
    path('<str:pk>/remove',RemoveFromBasketView.as_view(),name='remove_from_basket'),    
    path('myproducts/',MyProductsListView.as_view(),name='my_products'),
    path('<str:pk>/edit/',ProductEditView.as_view(),name='product_edit'),
    path('post/',CreateProductView.as_view(),name='create_product'),
    path('list/',ProductListView.as_view(),name='product_list'),
    path('<str:pk>/',ProductDetailView.as_view(),name='product_detail'),
    path('<str:pk>/delete/',ProductDeleteView.as_view(),name='product_delete'),
    path('<str:pk>/delete_confirmation/',ProductDeleteConfirmationView.as_view(),name='delete_confirmation'),
    path('<str:pk>/buy',BuyProductView.as_view(),name='buy_product')
]
    
