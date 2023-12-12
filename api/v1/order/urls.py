from django.urls import path
from api.v1.order import views


app_name = "order"

urlpatterns = [
    path("",views.create_purchase_order),
    path("<int:id>/",views.purchase_oder_details),
    path("<int:id>/issue_date/",views.update_issue_date),
    path("<int:id>/acknowledgment_date/",views.update_acknowledgment_date),
    path("<int:id>/delivery_date/",views.update_delivery_date),
    path("<int:id>/quality_rating/",views.update_quality_rating),
]