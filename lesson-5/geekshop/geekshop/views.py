from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

categories = ProductCategory.objects.all()
positions = Product.objects.all()[:4]


def main(request):
    new_position = Product.objects.all()[:6:-1]
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    else:
        basket = 'Гость'
    context = {
        'name_page': '',
        'categories': categories,
        'positions': positions,
        'n_positions': new_position,
        'basket': basket,
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- О нас',
    }
    return render(request, 'about.html', context=context)


def checkout(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- Обратная связь',
    }
    return render(request, 'checkout.html', context=context)


def contact(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- Контакты',
    }
    return render(request, 'contact.html', context=context)


def faqs(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- FAQ',
    }
    return render(request, 'faqs.html', context=context)


def productdetail(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- Детали',
    }
    return render(request, 'productdetail.html', context=context)


def shoppingcart(request):
    context = {
        'categories': categories,
        'positions': positions,
        'name_page': '- Корзина',
    }
    return render(request, 'shoppingcart.html', context=context)


def link_menu(request, pk=None):
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id__pk=pk).order_by('price')

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'inc_menu.html', context=context)
