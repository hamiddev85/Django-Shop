from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path("", views.payment_view, name= "payment"),
    path("confirm/", views.payment_confirm, name="payment_confirm"),
]