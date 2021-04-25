from django.contrib import admin
from django.urls import path
from .views import main, about, checkout, contact, faqs, productdetail, products, shoppingcart

urlpatterns = [
    path('', main),
    path('about/', about),
    path('checkout/', checkout),
    path('contact/', contact),
    path('faqs/', faqs),
    path('productdetail/', productdetail),
    path('products/', products),
    path('shoppingcart/', shoppingcart)
]
