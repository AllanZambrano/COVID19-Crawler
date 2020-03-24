import scrapy
from scrapy_djangoitem import DjangoItem
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
from cases.models import Case, Country

def clean_space(param):
    return param.strip(' ')

def clean_number(param):
    return param.strip().replace(',', '')

class DataItem(DjangoItem):
    django_model = Case
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
    deaths = scrapy.Field(
        input_processor= MapCompose(clean_space, clean_number),
        output_processor= TakeFirst()
    )

class CountryItem(DjangoItem):
    django_model = Country
    name = scrapy.Field(        
        input_processor= MapCompose(clean_number),
        output_processor= TakeFirst()
        )
    code = scrapy.Field(        
        input_processor= MapCompose(clean_number),
        output_processor= TakeFirst()
        )
