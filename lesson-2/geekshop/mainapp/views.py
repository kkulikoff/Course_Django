from django.shortcuts import render

def products(request):
    context = {
        'name_page': '- Каталог',
    }
    return render(request, 'products.html', context=context)
