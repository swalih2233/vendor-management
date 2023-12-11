from django.urls import path
from api.v1.order import views


app_name = "order"

urlpatterns = [
    path("",views.create_purchase_order),
    path("<int:id>/",views.purchase_oder_details),
]