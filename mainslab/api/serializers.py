from rest_framework import serializers

from api.models import Bills, Client


class ClientSerializer(serializers.ModelSerializer):
    count_org = serializers.SerializerMethodField()
    check_sum_all_org = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ("name", "count_org", "check_sum_all_org")

    def get_count_org(self, obj):
        return Client.objects.filter(organizations__client_name=obj.id).count()

    def get_check_sum_all_org(self, obj):
        checks = Bills.objects.filter(clinet_name=obj.id)
        sum_check = 0
        for check in checks:
            sum_check += check.check_sum
        return sum_check


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = "__all__"


class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()

    class Meta:
        fields = ["file_uploaded"]
