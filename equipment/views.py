from django.shortcuts import render
from .models import Asset
from .tables import AssetTable
from django_tables2.export.export import TableExport
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from .filters import AssetFilter
from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView

# Create your views here.
# def asset(request):
#     table = AssetTable(Asset.objects.all())
    
#     RequestConfig(request, paginate={'per_page': 25}).configure(table)
    
#     return render(request, 'equipment/asset.html', {'table': table})

# def asset_filter(request):
#     table = AssetTable(Asset.objects.all())
#     f = AssetFilter(request.GET, queryset=Asset.objects.all())
#     return render(request, 'equipment/asset_filter.html',{'filter': f,'table': table})


# def bootstrap(request):
#     '''Demonstrate the use of the bootstrap template'''

#     table = BootstrapTable(Asset.objects.all())
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)

#     return render(request, 'equipment/bootstrap_template.html', {
#         'table': table
#     })


class FilteredAssetListView(SingleTableMixin, FilterView):
    table_class = AssetTable
    model = Asset
    template_name = 'equipment/bootstrap_template.html'

    filterset_class = AssetFilter
