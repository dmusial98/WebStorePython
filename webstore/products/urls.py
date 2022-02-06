from django.urls import path
from . import views
from .api import views

# router = routers.DefaultRouter()
# router.register(r'products', views.ProductListView)


urlpatterns = [
    path('', views.ProductsListView.as_view(), name=None)
]