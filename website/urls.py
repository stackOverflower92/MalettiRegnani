from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^products/', views.products, name='products'),
    url(r'^product/(?P<product_id>[0-9])', views.show_product, name='show_product'),
    url(r'^modenese/', views.modenese, name='modenese'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
