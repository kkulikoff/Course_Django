"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainapp import urls
from . import settings
from .views import contact, main, about, checkout, faqs, productdetail, shoppingcart

app_name = 'geekshop'

urlpatterns = [
    path('', main, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('checkout/', checkout, name='checkout'),
    path('faqs/', faqs, name='faqs'),
    path('productdetail/', productdetail, name='productdetail'),
    path('shoppingcart/', shoppingcart, name='shoppingcart'),
    path('products/', include(urls, namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
