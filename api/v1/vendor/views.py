import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404
from vendor.models import Vendor, Perfomance
from .serializers import VendorSerializer, PerfomanceSerializer 


@api_view(["POST", "GET"])
@permission_classes ([AllowAny])
def vendor(request):
    if request.method == "POST":
        name = request.data.get('name')
        contact_details = request.data.get('contact_details')
        address = request.data.get('address')

        last_vendor = Vendor.objects.all().first()
        if last_vendor is not None:
            id = last_vendor.id
            vendor_code = f"VD00{id+1}" 
        else:
            vendor_code ="VD001"
        vendor = Vendor.objects.create(
            name = name,
            contact_details = contact_details,
            address = address,
            vendor_code = vendor_code
        )

        vendor.save()

        date = datetime.date.today()

        performance = Perfomance.objects.create(
            vendor=vendor,
            date=date
        )

        performance.save()

        response_data = {
            "status_code" : 6000,
            "message" :"Successfully created vendor"
        }

        return Response(response_data)
    elif request.method == "GET":
        instances = Vendor.objects.all()
        context = {
        "request" : request
        }
        serializer = VendorSerializer(instances, many = True, context = context)

        response_data = {
        "status_code" : 6000,
        "data" : serializer.data,
        }

        return Response(response_data)




@api_view(["PUT","GET","DELETE"])
@permission_classes ([AllowAny])
def update_vendor(request,id):
    instance = get_object_or_404(Vendor, id=id)

    if request.method == "GET":
        context ={
            "request":request
        }
        serializer = VendorSerializer(instance,context=context)


        response_data ={
            "status_code":6000,
            "data":serializer.data
        }
        return Response(response_data)
    
    elif request.method == "PUT":
        name = request.data.get('name')
        contact_details = request.data.get('contact_details')
        address = request.data.get('address')

        if name is not None:
            instance.name = name
            instance.save()

        if contact_details is not None:
            instance.contact_details = contact_details
            instance.save()

        if  address  is not None:
            instance.address = address
            instance.save()


        response_data ={
            "success_code":6000,
            "message":"vendor updated successfully"
        }
        return Response(response_data)
    

    elif request.method == "DELETE":
        instance.delete()

        response_data={
            "success_code":6000,
            "message":"vender deleted successfully"
        }

        return Response(response_data)





@api_view(["GET"])
@permission_classes ([AllowAny])
def perfomance(request,id):
    vendor = get_object_or_404(Vendor, id=id)

    instance = get_object_or_404(Perfomance,vendor=vendor)

    context ={
            "request":request
        }
    serializer = PerfomanceSerializer(instance,context=context)


    response_data ={
            "status_code":6000,
            "data":serializer.data
        }
    return Response(response_data)