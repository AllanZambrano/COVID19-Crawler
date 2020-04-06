import os
from django.contrib.gis.utils import LayerMapping
from .models import Country

world_mapping = {
    'iso2' : 'ISO2',
    'name' : 'NAME',
    'pop2005' : 'POP2005',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Country, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)