from django.db import models
from vendor.models import Vendor


class Order(models.Model):
    po_number=models.CharField()
    vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField()
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateField()

    
    class Meta:
        db_table = 'order_order'
        verbose_name = 'order'
        verbose_name_plural = 'order'
        ordering = ('-id',)

    def __str__(self):
        return self.po_number