from django.urls import path

from .views import TeamViewSet, TeamPositionViewSet

urlpatterns = [
    path("", TeamViewSet.as_view({"get": "list", "post":"create"})),
    path("/positions", TeamPositionViewSet.as_view({"get": "list", "post":"create"})),
]