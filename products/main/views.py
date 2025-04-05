from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product


@api_view(['GET'])
def products_list_view(request): 
    # """реализуйте получение всех товаров из БД
    # реализуйте сериализацию полученных данных
    # отдайте отсериализованные данные в Response"""
    if request.method == 'GET':
        all_products = Product.objects.all()
        serializer = ProductListSerializer(all_products, many=True)
        return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        # """реализуйте получение товара по id, если его нет, то выдайте 404
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404()
        if request.method == 'GET':
            serializer = ProductDetailsSerializer(product)
            return Response(serializer.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass

