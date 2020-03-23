from cases.models import Case

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        if item.get("deaths"):
            item.save()
            return item
        else:
            item["deaths"] = "0"
            item.save()
            return item

# https://stackoverflow.com/questions/23663459/how-to-update-djangoitem-in-scrapy/44997484
# It updates the bd, changed the PK to country to avoid duplication
class UpdatePipeline(object):
    def process_item(self, item, spider):
        try:
            case = Case.objects.get(country=item['country'])
            instance = item.save(commit=False)
            instance.pk = case.pk
        except Case.DoesNotExist:
            pass
        item.save()
        return item