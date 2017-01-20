from django.shortcuts import render
from models import *
from ipware.ip import get_ip
from django.contrib.gis.geoip2 import GeoIP2


# Create your views here.
def index(request):
    descriptions = Descriptions.objects.first()
    country_code = get_client_country(get_ip(request))

    context = {
        'descriptions': descriptions,
        'country_code': country_code,
    }

    return render(request, 'website/index.html', context)


def products(request):
    show_products = Product.objects.all()
    descriptions = Descriptions.objects.first()
    country_code = get_client_country(get_ip(request))

    context = {
        'descriptions': descriptions,
        'products': show_products,
        'country_code': country_code,
    }

    return render(request, 'website/products.html', context)


def show_product(request, product_id):
    product = Product.objects.get(id=product_id)
    descriptions = Descriptions.objects.first()
    country_code = get_client_country(get_ip(request))

    context = {
        'product': product,
        'descriptions': descriptions,
        'country_code': country_code,
    }

    return render(request, 'website/show_product.html', context)


def modenese(request):
    descriptions = Descriptions.objects.first()
    country_code = get_client_country(get_ip(request))

    context = {
        'descriptions': descriptions,
        'country_code': country_code,
    }

    return render(request, 'website/modenese.html', context)


def get_client_country(ip):
    g = GeoIP2()

    if ip is None:
        return 'IT'
    else:
        try:
            return g.country_code(ip)
        except:
            return 'IT'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
