import scrapy
from crawler.items import CrawlerCovidItem
from scrapy.loader import ItemLoader


class DataSpider(scrapy.Spider):
    name = "crawlercovid"
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.DuplicatePipeline': 300,

        }
    }

    allowed_domains = ['https://www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/coronavirus',
    ]

    def parse(self, response):
        for data in response.xpath("//*[@id='main_table_countries_today']/tbody[1]/tr"):
            l = ItemLoader(item=CrawlerCovidItem(), selector=data)
            l.add_xpath('country', './/td[1]')
            l.add_xpath('confirmed', './/td[2]/text()')
            l.add_xpath('active', './/td[7]/text()')
            l.add_xpath('new_cases', './/td[3]/text()')
            l.add_xpath('deaths', './/td[4]/text()')
            l.add_xpath('new_deaths', './/td[5]/text()')
            l.add_xpath('recovered', './/td[6]/text()')

            yield l.load_item()
