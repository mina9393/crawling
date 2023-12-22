import scrapy
from lxml import html
from scrapy import Request

class NoranSpider(scrapy.Spider):
    name='noran'
    start_urls=['https://nooraancollection.ir/shop/']
   

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url=url, headers=self.headers)
    #     # return super().start_requests()

    def parse(self, response):
        tree = html.fromstring(response.text)
        for item in tree:
            yield{
            'urls ': tree.xpath('//*[@class="product-title"]/a/@href'),
            "price": tree.xpath('//div[@id="primary"]//*[contains(@class,"woocommerce-Price-amount")]/bdi/text()'),
            
            }
        for item in response.xpath('//div[@id="primary"]//*[contains(@class,"product-wrapper")]'):
            yield{
            "title":item.xpath('//*[@class="product-title"/text()]')}