from user.views import ProfileViewSet
from django.urls import path

urlpatterns = [
    path("", ProfileViewSet.as_view({"get": "list", "post": "create"})),
    path("/<int:pk>", ProfileViewSet.as_view({"get": "retrieve"})),

]
