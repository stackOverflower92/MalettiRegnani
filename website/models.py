from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    name_it = models.CharField(max_length=200, verbose_name="Nome Prodotto in Italiano")
    description_it = models.TextField(verbose_name="Descrizione in Italiano")
    name_en = models.CharField(max_length=200, verbose_name="Nome Prodotto in Inglese")
    description_en = models.TextField(verbose_name="Descrizione in Inglese")
    image = models.ImageField(upload_to="uploads/images/products", verbose_name="Immagine")
    buy_url = models.URLField(verbose_name="URL per l'Acquisto")


class Descriptions(models.Model):
    class Meta:
        verbose_name = "Gruppo Descrizioni e Dettagli Sito"
        verbose_name_plural = "Gruppi Descrizioni e Dettagli Sito"

    main_description_it = models.TextField(verbose_name="Descrizione Principale in Italiano")
    main_description_en = models.TextField(verbose_name="Descrizione Principale in Inglese")
    tel = models.CharField(max_length=200, verbose_name="Numero di Telefono")
    email = models.EmailField(verbose_name="Indirizzo E-mail")
    fax = models.CharField(verbose_name="Numero Fax", max_length=200)
    store_page_url = models.URLField(verbose_name="URL della pagina dello store (quella contenente tutti i prodotti)")
    logo = models.ImageField(upload_to="uploads/images/descriptions", verbose_name="Logo Principale del Sito")
    site_name = models.CharField(max_length=200, verbose_name="Nome del Sito", default="Nome Sito")
    header_background = models.ImageField(upload_to="uploads/images/descriptions", verbose_name="Immagine di Sfondo (Testata)")
    modenese_it = models.TextField(verbose_name="Testo per pagina Modenese in Italiano", default="Modenese IT")
    modenese_en = models.TextField(verbose_name="Testo per pagina Modenese in Inglese", default="Modenese EN")
