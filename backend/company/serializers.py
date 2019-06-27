from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'email', 'web_site', 'logo_path')

    def create(self, validated_data):
        instance = Company.objects.create(**validated_data)
        return instance
