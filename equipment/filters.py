from django_filters import FilterSet

from .models import Asset


class AssetFilter(FilterSet):
    class Meta:
        model = Asset
        fields = {
            'asset_type': ['contains'],
            'owner': ['contains'],            
            'status': ['exact'],
            'assignee': ['contains'],
        }
