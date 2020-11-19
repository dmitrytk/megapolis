from rest_framework import serializers

from api.models import ContractView, Employee


class ContractViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractView
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'organization_id', 'first_name', 'last_name', 'position']
