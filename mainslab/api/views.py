from django.shortcuts import render
from rest_framework import status, viewsets

from api.models import Client, Organization, Bills
from api.serializers import ClientSerializer, CheckSerializer
from api.filters import OrgClientNameFilter


SERVICE_CHOICE = {
    1: 'консультация',
    2: 'лечение',
    3: 'стационар',
    4: 'диагностика',
    5: 'лаборатория'
}

class UploadeViewSet(viewsets.ModelViewSet):
    pass

class ClientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CheckViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = CheckSerializer
    filterset_fields = ('clinet_name', 'client_org') 
