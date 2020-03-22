import scrapy
from crawler.items import CrawlerItem
from scrapy.loader import ItemLoader


class CovidSpider(scrapy.Spider):
    name = "covid"
    
    allowed_domains = ['https://www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/coronavirus',
    ]

    def parse(self, response):
        for data in response.xpath("//*[@id='main_table_countries_today']/tbody[1]/tr"):
            l = ItemLoader(item=CrawlerItem(), selector=data)
            l.add_xpath('country', './/td[1]')
            l.add_xpath('total_cases', './/td[2]/text()')
            l.add_xpath('active_cases', './/td[7]/text()')
            l.add_xpath('total_deaths', './/td[4]/text()')

            yield l.load_item()