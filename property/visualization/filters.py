import django_filters
from input.models import Location

class PropertyFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    micro_market = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ['location', 'micro_market', 'city']
