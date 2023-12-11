from django.db import models
from vendor.models import Vendor


STATUS_CHOICES = (
    ("1","pending"),
    ("2","completed"),
    ("3","cancelled")
)



class Order(models.Model):
    po_number=models.CharField(max_length=150)
    vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(blank=True,null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=25,choices=STATUS_CHOICES)
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    acknowledgment_date = models.DateField(blank=True, null=True)

    
    class Meta:
        db_table = 'order_order'
        verbose_name = 'order'
        verbose_name_plural = 'order'
        ordering = ('-id',)

    def __str__(self):
        return self.po_number