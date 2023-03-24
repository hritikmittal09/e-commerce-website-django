from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("shop/",views.home),
    path("product_view/<product_id>",views.product_view),
    path("",views.login),
    path("signup",views.signup),
    path("check/",views.checkcadentails  ),
    path("cart/<product>/<product_prize>",views.add_cart ),
    path("cart_show/",views.cart_show ),
    path("delete/<product>",views.delete ),
    path("payment_sucess",views.payment_sucess )

    


    
]

