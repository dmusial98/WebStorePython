from urllib import request
from .models import Cart, CartProduct
from . import serializers
from rest_framework.permissions import AllowAny
# from . import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer
    # permission_classes = []
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['productId', 'productName', 'categoryType']
    # ordering = ['id']

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        super(CartCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        super(CartDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(CartDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(CartDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)


class ProductCartListView(generics.ListAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = serializers.CartProductSerializer
    # permission_classes = []
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['productId', 'productName', 'categoryType']
    # ordering = ['id']

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class ProductCartCreateView(generics.CreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = serializers.CartProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        super(ProductCartCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class ProductCartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = serializers.CartProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        super(ProductCartDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ProductCartDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ProductCartDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)