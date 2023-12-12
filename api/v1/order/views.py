import requests
import datetime
from django.db.models import Sum

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
def purchase_oder_details(request,id):
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
    

@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_issue_date(request,id):
    instance = get_object_or_404(Order, id=id)

    date = datetime.datetime.today()

    instance.issue_date = date
    instance.save()

    response_data={
        "success_code":6000,
        "message":"Issue date updated"
    }
 
    return Response(response_data)




@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_acknowledgment_date(request,id):
    instance = get_object_or_404(Order, id=id)

    date = request.data.get('date')

    acknowledgment_date = datetime.datetime.today()

    instance.expeted_delivery_date = date
    instance.acknowledgment_date = acknowledgment_date
    instance.save()

    vendor = instance.vendor

    total_orders = Order.objects.filter(vendor=vendor)
    total_orders_count = total_orders.count()


    total_response_time = 0

    if total_orders_count > 0:
        total_response_time = 0

        for order in total_orders:
            issue_date = order.issue_date
            acknowledgment_date = order.acknowledgment_date

            if issue_date is not None and acknowledgment_date is not None:
                response_time = (acknowledgment_date - issue_date).total_seconds()
                total_response_time += response_time

        average_response_time = total_response_time / total_orders_count
    else:
        average_response_time = 0 

    vendor.average_response_time = average_response_time / 60
    vendor.save()

    performance = get_object_or_404(Perfomance, vendor=vendor)
    performance.average_response_time = average_response_time
    performance.save()

    response_data={
        "success_code":6000,
        "message":"Delivery date updated"
    }
 
    return Response(response_data)


@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_delivery_date(request,id):
    instance = get_object_or_404(Order, id=id)

    date = datetime.datetime.today()

    instance.delivery_date = date
    instance.status = 2
    instance.save()

    vendor = instance.vendor

    total_orders = Order.objects.filter(vendor=vendor)
    order_count = total_orders.count()
    complted_orders = total_orders.filter(status=2).count()

    comptd_orders = total_orders.filter(status=2)

    fulfilment = complted_orders / order_count

    on_time_deliveries = 0

    for order in comptd_orders:
        expeted_delivery_date = order.expeted_delivery_date
        delivery_date = order.delivery_date


        if delivery_date <= expeted_delivery_date:
            on_time_deliveries += 1

    on_time_delivery_rate = (on_time_deliveries / complted_orders) * 100

    vendor.fulfillment_rate = fulfilment
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()

    performance = get_object_or_404(Perfomance, vendor=vendor)
    performance.fulfillment_rate = fulfilment
    vendor.on_time_delivery_rate = on_time_delivery_rate
    performance.save()

    response_data={
        "success_code":6000,
        "message":"Delivery date updated",
    }
 
    return Response(response_data)


@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_quality_rating(request,id):
    instance = get_object_or_404(Order, id=id)

    rate = request.data.get('rate')

    if int(rate) > 5:
        rate =5

    instance.quality_rating = rate
    instance.save()

    vendor = instance.vendor

    total_orders = Order.objects.filter(vendor=vendor)
    order_count = total_orders.count()
    total_quality_rating = total_orders.aggregate(Sum("quality_rating"))["quality_rating__sum"]
    vendor_rating = total_quality_rating / order_count

    vendor.quality_rating_avg = vendor_rating
    vendor.save()

    performance = get_object_or_404(Perfomance, vendor=vendor)
    performance.quality_rating_avg = vendor_rating
    performance.save()


    response_data={
        "success_code":6000,
        "message":"Quality rate updated"
    }
 
    return Response(response_data)

