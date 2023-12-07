from django.urls import path
from api.v1.order import views


app_name = "order"

urlpatterns = [
    path("",views.create_purchase_order),
    path("",views.purchase_order_list),
    path("<int:id>/",views.purchase_oder_details),
    path("<int:id>/",views.update_purchase_order),
    path("<int:id>/",views.delete_purchase_order),

]