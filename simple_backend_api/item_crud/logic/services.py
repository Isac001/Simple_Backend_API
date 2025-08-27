from ..models import Item
from decimal import Decimal
from . import selectors
from .validation_erros import ValidationError

def create_item(*, name_item: str, value_item: float, quantity_item: int, description_item: str) -> Item:

    errors = []

    if not name_item or len(name_item) < 3:

        errors.append("O nome do item deve ter ao menos três caracteres.")

    if value_item <= Decimal(0.0):

        errors.append("O valor do item deve ser maior que zero.")

    if quantity_item < 0:

        errors.append("A quantidade do item não pode ser negativa.")

    if errors:

        raise ValidationError(errors)

    new_item = selectors.item_create(
        name_item=name_item,
        value_item=value_item,
        quantity_item=quantity_item,
        description_item=description_item
    )

    return new_item

def update_item(*, item: selectors.item_detail, data: dict) -> Item:
    
    errors = []

    name_item = data.get('name_item', item.name_item)
    value_item = data.get('value_item', item.value_item)
    quantity_item = data.get('quantity_item', item.quantity_item)
    description_item = data.get('description_item', item.description_item)

    if not name_item or len(name_item) < 3:

        errors.append("O nome do item deve ter ao menos três caracteres.")

    if value_item <= Decimal(0.0):

        errors.append("O valor do item deve ser maior que zero.")

    if quantity_item < 0:
        
        errors.append("A quantidade do item não pode ser negativa.")

    if errors:

        raise ValidationError(errors)
    
    update_item = selectors.item_update(
        pk=item.pk,
        name_item=name_item,
        value_item=value_item,
        quantity_item=quantity_item,
        description_item=description_item
    )

    return update_item