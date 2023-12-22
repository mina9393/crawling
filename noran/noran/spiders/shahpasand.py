import scrapy
from lxml import html
from scrapy import Request
import re

class ShahpasandSpider(scrapy.Spider):
    name='shahpasand'
    start_urls=['https://boutiqueshahpasand.com/product/%d9%8a%d9%82%d9%87-%d9%81%d9%8a%d9%83-%d9%88-%d8%af%d8%a7%d9%85%d9%86%d9%83-%d9%85%d9%86%d8%a7%d8%b3%d8%a8-%d8%a8%d8%b1%d8%a7%d9%89-%d8%b2%d9%8a%d8%b1-%d8%a8%d8%a7%d9%81%d8%aa-%d9%88-%d8%af%d9%88/']
    max_page=10

    def start_requests(self):
        for i in range(int(self.max_page)):
            yield Request(url=f'https://boutiqueshahpasand.com/page/{i + 1}')
      
        

    def parse(self, response):
        tree = html.fromstring(response.text)
        # for item in tree:
            # yield{
            # 'urls ': tree.xpath('//*[@class="wd-entities-title"]/a/@href'),
            # 'title ': tree.xpath('//*[@class="wd-entities-title"]/a/text()'),
        id = tree.xpath('//*[@class="wd-entities-title"]/a/@href')
        # id_2 =  re.findall(r'\d+', str(id[0]))
        print(id)
            
            # "price": tree.xpath('//div[@id="primary"]//*[contains(@class,"woocommerce-Price-amount")]/bdi/text()'),
            
            # }