from django.urls import path
from api.v1.vendor import views

app_name = "vendor"

urlpatterns = [
    # path("",views.create_vendor),
    path("",views.vendors_list),
    path("<int:id>/",views.vendor_details),
    path("<int:id>/",views.update_vendor),
    path("<int:id>/",views.delete_vendor),
    path("<int:id>/perfomance/",views.perfomance),

    ]