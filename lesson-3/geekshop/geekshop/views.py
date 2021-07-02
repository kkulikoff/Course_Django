from django.shortcuts import render
from mainapp.models import Product, ProductCategory

categories = ProductCategory.objects.all()
positions = Product.objects.all()[:4]


def main(request):
    new_position = Product.objects.all()[:6:-1]
    context = {
        'name_page': '',
        'categories': categories,
        'positions': positions,
        'n_positions': new_position
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


def link_menu(request):
    links_menu = {'links': [
            {'href': 'products:index', 'name': 'Категория'},
            {'href': 'products:index', 'name': 'Категория'},
            {'href': 'products:index', 'name': 'Категория'},
            {'href': 'products:index', 'name': 'Категория'},
            {'href': 'products:index', 'name': 'Категория'}
        ]}
    return render(request, 'inc_menu.html', context=links_menu)
