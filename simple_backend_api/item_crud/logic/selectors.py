from django.db.models import QuerySet
from decimal import Decimal
from ..models import Item

def item_list() -> QuerySet[Item]:

    return Item.objects.all().order_by('client_name')

def item_detail(*, pk: int) -> Item:

    return Item.objects.get(pk=pk)

def item_create(*, name_item: str, value_item: Decimal, quantity_item: int, description_item: str ) -> Item:

    return Item.objects.create(
        name_item=name_item,
        value_item=value_item,
        quantity_item=quantity_item,
        description_item=description_item
    )

def item_update(*, pk: int, name_item: str, value_item: Decimal, quantity_item: int, description_item: str) -> Item:

    item_to_update = Item.objects.get(pk=pk)

    item_to_update.name_item = name_item
    item_to_update.value_item = value_item
    item_to_update.quantity_item = quantity_item
    item_to_update.description_item = description_item

    item_to_update.save()

    return item_to_update

def item_delete(*, pk: int) -> None:

    item = Item.objects.get(pk=pk)
    item.delete()
    return {'Status': 'Deleted'}