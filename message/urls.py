from django.urls import path

from .views import MessageViewSet

urlpatterns = [
    path("", MessageViewSet.as_view({"get": "list", "post":"create"})),
    path("/<int:pk>", MessageViewSet.as_view({"get": "retrieve", "post":"accept"})),
]