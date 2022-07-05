from rest_framework import serializers
from api.models import Client, Organization, Bills

class ClientSerializer(serializers.ModelSerializer):
    count_org = serializers.SerializerMethodField()
    check_sum_all_org = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ('name', 'count_org', 'check_sum_all_org')
    
    def get_count_org(self, obj):
        return Client.objects.filter(organizations__client_name=obj.id).count()

    #TODO работает не верно
    def get_check_sum_all_org(self, obj):
        # return Client.objects.aggregate(bills_check_sum=Sum('bills'))
        return Client.objects.filter(bills__client_name=obj.name)

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'
