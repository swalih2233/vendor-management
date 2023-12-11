from vendor.models import Vendor,Perfomance
from rest_framework.serializers import ModelSerializer 


class VendorSerializer(ModelSerializer):
    class Meta:
        fields = ("id","name","contact_details","address","vendor_code","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate")
        model = Vendor



class PerfomanceSerializer(ModelSerializer):
    class Meta:
        fields = ("id","vendor","date","on_time_delivery_rate","average_response_time","fulfillment_rate")
        model = Perfomance