from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100,unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    
    class Meta:
        db_table = 'vendor_vendor'
        verbose_name = 'vendor'
        verbose_name_plural = 'vendor'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Perfomance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    
    class Meta:
        db_table = 'vendor_perfomance'
        verbose_name = 'pefomance'
        verbose_name_plural = 'perfomance'
        ordering = ('-id',)

    def __str__(self):
        return self.vendor.name