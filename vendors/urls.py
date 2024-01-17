from django.urls import path
from . import views


app_name = "vendors"

urlpatterns = [
    path("request/", views.index, name="request"),
    path("dashboard/", views.dashboard, name="dashboard"),

]
