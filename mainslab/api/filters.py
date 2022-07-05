from http.client import FAILED_DEPENDENCY
from django_filters import rest_framework as filters
from django_filters import AllValuesMultipleFilter

from api.models import Bills


class OrgClientNameFilter(filters.FilterSet):
    org = AllValuesMultipleFilter(field_name='client_org')
    name = AllValuesMultipleFilter(field_name='client_name')

    class Meta:
        model = Bills
        fields = ['name', 'org']
