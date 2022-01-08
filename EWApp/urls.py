from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('order/', views.order, name="order"),
    path('seller/', views.seller, name="seller"),
]