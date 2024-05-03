from django.shortcuts import render

from courier_app.decorator import permission_required
from . models import Product
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from .blog_serializer import BlogSerializer
from utils.base_authentication import JWTAuthentication
from .courier_controller import OrderController, ProductController
from rest_framework.permissions import IsAdminUser
# Create your views here.

# product_controller = ProductController()
order_controller = OrderController()
product_controller = ProductController()

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
    

class ProductViews(ModelViewSet):
    authentication_classes = [JWTAuthentication] 

# permission_classes = [IsAdminUser]

    @permission_required(['create_product'])
    def post_product(self, request):
        return product_controller.create(request)


    @permission_required(['read_product'])
    def get_product(self, request):
        return product_controller.get_product(request)


    @permission_required(['update_product'])
    def update_product(self, request):
        return product_controller.update_product(request)

    @permission_required(['delete_product'])
    def delete_product(self, request):
        return product_controller.delete_product(request)
    