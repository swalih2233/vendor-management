import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404
from order.models import Order
from .serializers import OrderSerializer

@api_view(["POST","GET"])
@permission_classes ([AllowAny])
def create_purchase_order(request,id):
     if request.method == "POST":
        po_number = request.data.get('po_number')
        vendor = request.data.get('vendor')
        order_date= request.data.get('order_date')
        items = request.data.get('items')
        quantity = request.data.get('quantity')
        status = request.data.get('status')

        last_vendor = Order.objects.all().first()
        if last_vendor is not None:
            id = last_vendor.id
            vendor_code = f"VD00{id+1}" 
        else:
            vendor_code ="VD001"
        vendor = Order.objects.create(
            po_number = po_number,
            vendor = vendor,
            order_date = order_date,
            items = items,
            quantity = quantity,
            status = status,
            vendor_code = vendor_code
        )

        vendor.save()

        response_data = {
            "status_code" : 6000,
            "message" :"Successfully created vendor"
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
    elif request.method == "PUT":
        pass
    

    elif request.method == "DELETE":
        instance.delete()

        response_data={
            "success_code":6000,
            "message":"vender deleted successfully"
        }

        return Response(response_data)




