import django_filters
from .models import *
from django import forms

class PropertyFilter(django_filters.FilterSet):


    # property_purpose = django_filters.ModelChoiceFilter(
    #     field_name='property_purpose', lookup_expr='isnull',
    #     null_label='Uncategorized',
    #     queryset=Property.objects.all(),
    # )
    class Meta:
        model = Property
        # fields='__all__'
        # exclude =('property_types_img')
        fields = ['property_purpose', 'city']
        
