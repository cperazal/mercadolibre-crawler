import scrapy
from scrapy.http import Request

def clearSpaces(text):
    if text is None:
        text = ""
    else:
        text = " ".join(text.split())
    return text

class ProductosSpider(scrapy.Spider):
    name = 'productos'
    allowed_domains = ['www.mercadolibre.com.ve',
                       'listado.mercadolibre.com.ve',
                       'articulo.mercadolibre.com.ve']
    start_urls = ['https://listado.mercadolibre.com.ve/']

    def __init__(self, search):
        self.start_urls = {self.start_urls[0] + search}

    def parse(self, response):
        products = response.xpath('//*[@class="ui-search-result__content ui-search-link"]/@href').extract()
        for product in products:
            absolute_url = response.urljoin(product)
            yield Request(absolute_url, callback=self.parse_product)

        # pagina siguiente
        next_page_url = response.xpath('//li[@class="andes-pagination__button andes-pagination__button--next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_product(self, response):
        titulo = response.xpath('//h1//text()').extract_first()
        descripcion = response.xpath('//*[@class="item-description__text"]/p/text()').extract_first()
        condiciones = response.xpath('//*[@class="item-conditions"]//text()').extract_first()
        precio_miles = response.xpath('//*[@id="productInfo"]//span/span[2]//text()').extract_first()
        precio_decimales = response.xpath('//*[@id="productInfo"]//span/span[4]//text()').extract_first()
        precio = str(precio_miles) + ',' + str(precio_decimales) if precio_decimales is not None else str(precio_miles)
        color = response.xpath('//*[@data-id="COLOR_SECONDARY_COLOR"]//strong//text()').extract_first()
        disponible = response.xpath('//*[@class="dropdown-quantity-units"]//text()').extract_first()
        #imagen_url = response.xpath('//*[@id="gallery_dflt"]//figure[1]/a/@href').extract_first()
        ubicacion = response.xpath('//*[@class="card-description text-light"]/@title').extract_first()
        reputacion = response.xpath('//*[@class="reputation-relevant"][1]/strong/text()').extract_first()
        antiguedad_mercadolibre = response.xpath('//*[@class="history-data"][1]/text()').extract_first()
        ventas_concretadas = response.xpath('//*[@class="reputation-relevant"][2]/strong/text()').extract_first()
        url = response.url

        yield {
            'titulo': clearSpaces(titulo),
            'descripcion': clearSpaces(descripcion),
            'condiciones': clearSpaces(condiciones),
            'precio': clearSpaces(precio),
            'color': clearSpaces(color),
            'disponible': clearSpaces(disponible),
            #'imagen_url': clearSpaces(imagen_url),
            'ubicacion': clearSpaces(ubicacion),
            'reputacion': clearSpaces(reputacion),
            'antiguedad_vendedor': clearSpaces(antiguedad_mercadolibre),
            'ventas_concretadas': clearSpaces(ventas_concretadas),
            'url': url
        }

