from CrawledData.models import CrawlerCovid

class DataPipeline(object):
    def process_item(self, item, spider):
        try:
            data = CrawlerCovid.objects.get(country=item['country'])
            instance = item.save(commit=False)
            instance.pk = data.pk
        except CrawlerCovid.DoesNotExist:
            pass
        item.save()
        return item
