from order.models import Order
from rest_framework.serializers import ModelSerializer 

class OrderSerializer(ModelSerializer):
    class Meta:
        fields = ("id"," po_number","vendor","order_date","delivery","items","quantity","status","quality_rating","issue_date","acknowledgment_date")
        model = Order