from rest_framework import serializers
from .models import Entity


class Serializer(serializers.ModelSerializer):

    cost = serializers.SerializerMethodField(method_name="calc_cost")
    class Meta:
        model = Entity
        fields = '__all__'

    def calc_cost(self, instance):
        return instance.amount * instance.price
