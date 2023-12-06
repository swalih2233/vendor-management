import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny


from vendor.models import Vendor, Perfomance

@api_view(["POST"])
@permission_classes ([AllowAny])
def create_vendor(request):
    pass

@api_view(["GET"])
@permission_classes ([AllowAny])
def vendors_list(request):
    pass

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