# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-02 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description_it', models.TextField(verbose_name='Descrizione Principale in Italiano')),
                ('main_description_en', models.TextField(verbose_name='Descrizione Principale in Inglese')),
                ('tel', models.CharField(max_length=200, verbose_name='Numero di Telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Indirizzo E-mail')),
                ('fax', models.CharField(max_length=200, verbose_name='Numero Fax')),
                ('store_page_url', models.URLField(verbose_name='URL della pagina dello store (quella contenente tutti i prodotti)')),
                ('logo', models.ImageField(upload_to='images/descriptions', verbose_name='Logo Principale del Sito')),
                ('site_name', models.CharField(max_length=200, verbose_name='Nome del Sito')),
                ('header_background', models.ImageField(upload_to='images/descriptions', verbose_name='Immagine di Sfondo (Testata)')),
            ],
            options={
                'verbose_name': 'Gruppo Descrizioni e Dettagli Sito',
                'verbose_name_plural': 'Gruppi Descrizioni e Dettagli Sito',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_it', models.CharField(max_length=200, verbose_name='Nome Prodotto in Italiano')),
                ('description_it', models.TextField(verbose_name='Descrizione in Italiano')),
                ('name_en', models.CharField(max_length=200, verbose_name='Nome Prodotto in Inglese')),
                ('description_en', models.TextField(verbose_name='Descrizione in Inglese')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='Immagine')),
                ('buy_url', models.URLField(verbose_name="URL per l'Acquisto")),
            ],
            options={
                'verbose_name': 'Prodotto',
                'verbose_name_plural': 'Prodotti',
            },
        ),
    ]
