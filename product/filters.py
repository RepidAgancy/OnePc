import django_filters
from product import models

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    color = django_filters.ModelMultipleChoiceFilter(
        queryset=models.ProductColour.objects.all(),
        field_name='colours__colour', 
        label='Color',
        to_field_name='colour',
    )
    brand = django_filters.ModelChoiceFilter(queryset=models.BrandProduct.objects.all(), label='Brand')

    info_name = django_filters.CharFilter(
        field_name='components__info_name',
        lookup_expr='icontains',
        label='Component Name'
    )
    info_text = django_filters.CharFilter(
        field_name='components__info_text',
        lookup_expr='icontains',
        label='Component Value'
    )
    class Meta:
        model = models.Product
        fields = ['price', 'brand', 'color', 'info_name', 'info_text'] 
