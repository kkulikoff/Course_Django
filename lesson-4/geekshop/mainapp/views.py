from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def products(request):
    positions_body = Product.objects.all()[:10]
    categories = ProductCategory.objects.all()
    positions = Product.objects.all()[:4]
    context = {
        'name_page': '- Каталог',
        'products': positions_body,
        'categories': categories,
        'positions': positions,
    }
    return render(request, 'products.html', context=context)
