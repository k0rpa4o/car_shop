from django.urls import path
from .views import ProductView, ProductFilter

urlpatterns = [
   path('', ProductView.as_view(), name="all-product"),
   path("product/<str:name>", ProductFilter.as_view(), name="product"),
]