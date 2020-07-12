# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadolibreItem(scrapy.Item):
    titulo = scrapy.Item()
    descripcion = scrapy.Item()
    condiciones = scrapy.Item()
    precio = scrapy.Item()
    color = scrapy.Item()
    disponible = scrapy.Item()
    imagen_url = scrapy.Item()
    ubicacion = scrapy.Item()
    reputacion = scrapy.Item()
    antiguedad_mercadolibre = scrapy.Item()
    ventas_concretadas = scrapy.Item()
    url = scrapy.Item()
