import django_tables2 as tables
from .models import Asset

class AssetTable(tables.Table):
    class Meta:
        model = Asset
        template = 'django_tables2/bootstrap.html'