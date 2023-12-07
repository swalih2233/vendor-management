import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


from vendor.models import Vendor, Perfomance
from .serializers import VendorSerializer


@api_view(["POST"])
@permission_classes ([AllowAny])
def create_vendor(request):
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

   response_data = {
       "status_code" : 6000,
       "message" :"Successfully created vendor"
   }

   return Response(response_data)

@api_view(["GET"])
@permission_classes ([AllowAny])
def vendors_list(request):
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

@api_view(["GET"])
@permission_classes ([AllowAny])
def vendor_details(request):
    pass

@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_vendor(request):
    pass

@api_view(["DELETE"])
@permission_classes ([AllowAny])
def delete_vendor(request):
    pass

@api_view(["GET"])
@permission_classes ([AllowAny])
def perfomance(request):
    pass