from django.shortcuts import render


def main(request):
    context = {
        'name_page': '',
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {
        'name_page': '- О нас',
    }
    return render(request, 'about.html', context=context)


def checkout(request):
    context = {
        'name_page': '- Обратная связь',
    }
    return render(request, 'checkout.html', context=context)


def contact(request):
    context = {
        'name_page': '- Контакты',
    }
    return render(request, 'contact.html', context=context)


def faqs(request):
    context = {
        'name_page': '- FAQ',
    }
    return render(request, 'faqs.html', context=context)


def productdetail(request):
    context = {
        'name_page': '- Детали',
    }
    return render(request, 'productdetail.html', context=context)


def shoppingcart(request):
    context = {
        'name_page': '- Корзина',
    }
    return render(request, 'shoppingcart.html', context=context)