from CrawledData.models import CrawlerCovid, Country
from scrapy.exceptions import DropItem

# https://stackoverflow.com/questions/23663459/how-to-update-djangoitem-in-scrapy/44997484
class DuplicatePipeline(object):
    def process_item(self, item, spider):
        try:
            item['country'] = Country.objects.get(name=item['country'])
            data = CrawlerCovid.objects.get(country=item['country'])
            instance = item.save(commit=False)
            instance.pk = data.pk
        except Country.DoesNotExist:
            raise DropItem("Missing country in %s" % item['country'])
        item['country'] = Country.objects.get(name=item['country'])
        item.save()
        return item
