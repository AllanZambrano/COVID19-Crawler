import scrapy
from crawler.items import CrawlerItem
from scrapy.loader import ItemLoader


class DataSpider(scrapy.Spider):
    name = "data_covid"

    allowed_domains = ['https://www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/coronavirus',
    ]

    def parse(self, response):
        for data in response.xpath("//*[@id='main_table_countries_today']/tbody[1]/tr"):
            l = ItemLoader(item=CrawlerItem(), selector=data)
            l.add_xpath('country', './/td[1]')
            l.add_xpath('confirmed', './/td[2]/text()')
            l.add_xpath('active', './/td[7]/text()')
            l.add_xpath('deaths', './/td[4]/text()')

            yield l.load_item()
