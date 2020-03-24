from cases.models import Case, Country

class CountryPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

class DataPipeline(object):
    def process_item(self, item, spider):
        item['country'] = Country.objects.get(name=item['country'])
        item.save()
        return item
       

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