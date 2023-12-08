from django.urls import path
from api.v1.vendor import views

app_name = "vendor"

urlpatterns = [
    path("",views.vendor),
    path("<int:id>/",views.update_vendor),
    path("<int:id>/perfomance/",views.perfomance),

    ]