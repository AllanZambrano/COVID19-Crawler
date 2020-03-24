import scrapy
from crawler.items import CountryItem
from scrapy.loader import ItemLoader


class DataSpider(scrapy.Spider):
    name = "countries"

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.CountryPipeline': 300,
        }
    }

    allowed_domains = ['https://countrycode.org/']
    start_urls = [
        'https://countrycode.org/',
    ]

    def parse(self, response):
        for data in response.xpath("//*[@class='table table-hover table-striped main-table']/tbody/tr"):
            l = ItemLoader(item=CountryItem(), selector=data)
            l.add_xpath('name', './/td[1]/a/text()')
            l.add_xpath('code', './/td[3]/text()')

            yield l.load_item()
