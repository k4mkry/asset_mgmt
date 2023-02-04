from django_filters import FilterSet, DateFilter, CharFilter
from .models import Asset


class AssetFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Asset
        fields = '__all__'
        exclude = [
            'purchase_date',
            'added_date',
            'image'
        ]
