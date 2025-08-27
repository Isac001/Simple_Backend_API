from . models import Item
from .logic import services
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = ['id', 'name_item', 'value_item', 'quantity_item', 'description_item']

    def validate(self, data):
        
        errors = []

        if "name_item" in data and len(data["name_item"]) < 3:
            errors.append("O nome do item deve ter ao menos três caracteres.")

        if "value_item" in data and data["value_item"] <= 0:
            errors.append("O valor do item deve ser maior que zero.")

        if "quantity_item" in data and data["quantity_item"] < 0:
            errors.append("A quantidade do item não pode ser negativa.")

        if errors:
            raise serializers.ValidationError({"errors": errors})

        return data
    
    def create(self, validated_data):

        return services.create_item(**validated_data)
    
    def update(self, instance, validated_data):

        return services.update_item(item=instance, data=validated_data)