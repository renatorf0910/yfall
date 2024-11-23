# models.py
from django.db import models
from .constants import ITEM_STATUS, ITEM_TYPE

class Item(models.Model):
    ITEM_STATUS_CHOICES = [
        (ITEM_STATUS['AVAILABLE'], 'Available'),
        (ITEM_STATUS['OUT_OF_STOCK'], 'Out of Stock'),
        (ITEM_STATUS['DISCONTINUED'], 'Discontinued'),
    ]
    
    ITEM_TYPE_CHOICES = [
        (ITEM_TYPE['PRODUCT'], 'Product'),
        (ITEM_TYPE['SERVICE'], 'Service'),
    ]

    item_image = models.ImageField(upload_to='items/', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    type = models.PositiveSmallIntegerField(choices=ITEM_TYPE_CHOICES)
    item_status = models.PositiveSmallIntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS['AVAILABLE'])
    color = models.CharField(max_length=50, null=True, blank=True)
    available = models.BooleanField(default=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.name
