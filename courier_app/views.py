from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from . models import Product
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from .blog_serializer import BlogSerializer
from utils.base_authentication import JWTAuthentication
from .courier_controller import ProductController, OrderController

from rest_framework.permissions import IsAdminUser
# Create your views here.

product_controller = ProductController()
order_controller = OrderController()


class OrderViews(ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def post_order(self, request):
        return order_controller.create(request)

    def get_order(self, request):
        return order_controller.get_order(request)

    def update_order(self, request):
        return order_controller.update_order(request)

    def delete_order(self, request):
        return order_controller.delete_order(request)
    