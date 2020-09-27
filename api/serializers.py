from rest_framework import serializers
from main.models import Product, Contractor, Operation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['username', 'operation', 'dt_created']
