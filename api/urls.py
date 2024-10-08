from django.urls import include, path

from rest_framework.authtoken import views

from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("category/", include("api.category.urls")),
    path("product/", include("api.product.urls")),
]