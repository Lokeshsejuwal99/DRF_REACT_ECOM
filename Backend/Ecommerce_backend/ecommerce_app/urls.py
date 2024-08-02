from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('products/', views.get_products, name='products'),
    path('', views.get_message, name="message")
]
