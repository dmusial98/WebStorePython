"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import token
from products.api import views
from users.views import UserListView, UserCreateView, UserDetailView
from carts.views import CartListView, ProductCartCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', )
    path('products/', views.ProductListView.as_view()),
    path('products/create/', views.ProductCreateView.as_view(), name=None),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name=None),
    path('users/', UserListView.as_view()),
    path('users/create/', UserCreateView.as_view(), name=None),
    # path('users/<int:pk>/', UserDetailView.as_view(), name=None),
    re_path('^users/byName/(?P<name>.+)/$', UserDetailView.as_view(), name=None),
    path('carts/', CartListView.as_view(), name=None ),
    path('carts/add/', ProductCartCreateView.as_view(), name=None),
    path('api/token/', token.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
