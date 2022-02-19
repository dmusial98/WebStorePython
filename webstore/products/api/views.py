from urllib import request
from ..models import Product
from . import serializers
from rest_framework.permissions import AllowAny
from . import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['productId', 'productName', 'categoryType']
    ordering = ['id']

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        super(ProductCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        super(ProductDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ProductDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ProductDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)