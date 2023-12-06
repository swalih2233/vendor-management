import requests
import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from order.models import Order

@api_view(["POST"])
@permission_classes ([AllowAny])
def create_purchase_order(request):
    pass

@api_view(["GET"])
@permission_classes ([AllowAny])
def purchase_order_list(request):
    pass

@api_view(["GET"])
@permission_classes ([AllowAny])
def purchase_oder_details(request):
    pass

@api_view(["PUT"])
@permission_classes ([AllowAny])
def update_purchase_order(request):
    pass

@api_view(["DELETE"])
@permission_classes ([AllowAny])
def delete_purchase_order(request):
    pass