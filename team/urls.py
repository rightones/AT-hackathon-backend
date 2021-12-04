from django.urls import path

from .views import TeamViewSet

urlpatterns = [
    path("", TeamViewSet.as_view({"get": "list", "post":"create"})),
]