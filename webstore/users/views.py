from cgitb import lookup
from urllib import request
from .models import User
from . import serializers
from rest_framework.permissions import AllowAny
# from . import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = []
    filter_backends = [DjangoFilterBackend]
    ordering = ['name']

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        super(UserCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name'] 
        return User.objects.filter(name = name)

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        super(UserDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(UserDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(UserDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)