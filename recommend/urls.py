from django.urls import path

from .views import TopicViewSet

urlpatterns = [
    path("topics", TopicViewSet.as_view({"get": "list", "post":"create"})),
]