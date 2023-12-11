import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404
from order.models import Order
from vendor.models import Vendor, Perfomance
from .serializers import OrderSerializer

@api_view(["POST","GET"])
@permission_classes ([AllowAny])
def create_purchase_order(request):
     if request.method == "POST":
        vendor = request.data.get('vendor')
        items = request.data.get('items')
        quantity = request.data.get('quantity')

        vendor = Vendor.objects.get(id=vendor)

        last_order = Order.objects.all().first()
        if last_order is not None:
            id = last_order.id
            po_number = f"ORD00{id+1}" 
        else:
            po_number ="ORD001"
        order = Order.objects.create(
            po_number = po_number,
            vendor = vendor,
            items = items,
            quantity = quantity,
            status = 1,
        )

        order.save()

        response_data = {
            "status_code" : 6000,
            "message" :"Successfully purchased"
        }

        return Response(response_data)
     elif request.method == "GET":
        instances = Order.objects.all()
        context = {
        "request" : request
        }
        serializer = OrderSerializer(instances, many = True, context = context)

        response_data = {
        "status_code" : 6000,
        "data" : serializer.data,
        }

        return Response(response_data)



@api_view(["GET","DELETE"])
@permission_classes ([AllowAny])
def purchase_oder_details(request):
    instance = get_object_or_404(Order, id=id)
  
    if request.method == "GET":
        context ={
            "request":request
        }
        serializer = OrderSerializer(instance,context=context)


        response_data ={
            "status_code":6000,
            "data":serializer.data
        }
        return Response(response_data) 

    elif request.method == "DELETE":
        instance.delete()

        response_data={
            "success_code":6000,
            "message":"vender deleted successfully"
        }

        return Response(response_data)




