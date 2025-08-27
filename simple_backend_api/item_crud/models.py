from django.db import models

class Item(models.Model):

    name_item = models.CharField(max_length=128, null=False)
    value_item = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity_item = models.IntegerField(null=False, default=0)
    description_item = models.TextField(null=True, default='Descrição não informada.')

    def __str__(self):

        return self.name_item
    
    class Meta:

        db_table = "item_crud"
        app_label = "item_crud"