from django.urls import path
from . import views


urlpatterns = [
    # Product
    path("product/", views.GetCreateProduct.as_view(), name='product-list'),
    path("product/<int:pk>/update/", views.UpdateProduct.as_view(), name='product-update'),
    path("product/<int:pk>/delete/", views.DeleteProduct.as_view(), name='delate-product'),

    # Customer
    path("customer/", views.GetCreateCustomer.as_view(), name='customer-list'),
    path("customer/<int:pk>/update/", views.UpdateCustomer.as_view(), name='customer-update'),
    path("customer/<int:pk>/delete/", views.DeleteCustomer.as_view(), name='delete-customer'),

    # orders
    path("orders/", views.OrderListCreateAPIView.as_view(), name='order-list'),
    path("orders/<int:pk>/", views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-details')
]