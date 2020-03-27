import scrapy
from scrapy_djangoitem import DjangoItem
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
from CrawledData.models import CrawlerCovid

def clean_space(param):
    return param.strip(' ')

def clean_number(param):
    return param.strip().replace(',', '')

def clean_plus(param):
    return param.strip().replace('+', '')


class CrawlerCovidItem(DjangoItem):
    django_model = CrawlerCovid
    country = scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor= TakeFirst()
    )
    confirmed = scrapy.Field(
        input_processor= MapCompose(clean_number),
        output_processor= TakeFirst()
    )
    active = scrapy.Field(
        input_processor= MapCompose(clean_number),
        output_processor= TakeFirst()
    )
    new_cases = scrapy.Field(
        default=0,
        input_processor=MapCompose(clean_space, clean_number, clean_plus),
        output_processor=TakeFirst()
    )
    deaths = scrapy.Field(
        default=0,
        input_processor= MapCompose(clean_space, clean_number, clean_plus),
        output_processor= TakeFirst()
    )
    new_deaths = scrapy.Field(
        default=0,
        input_processor= MapCompose(clean_space, clean_number, clean_plus),
        output_processor= TakeFirst()
    )
    recovered = scrapy.Field(
        default=0,
        input_processor=MapCompose(clean_space, clean_number),
        output_processor=TakeFirst()
    )