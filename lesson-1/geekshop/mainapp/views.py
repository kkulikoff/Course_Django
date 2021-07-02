from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def checkout(request):
    return render(request, 'mainapp/checkout.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def faqs(request):
    return render(request, 'mainapp/faqs.html')


def productdetail(request):
    return render(request, 'mainapp/productdetail.html')


def products(request):
    return render(request, 'mainapp/products.html')


def shoppingcart(request):
    return render(request, 'mainapp/shoppingcart.html')
