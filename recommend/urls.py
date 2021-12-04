from django.urls import path

from .views import TopicViewSet, AdeptTopicProfileViewSet, InterestTopicProfileViewSet

urlpatterns = [
    path("positions", TopicViewSet.as_view({"get": "list"})),
    path("topics", TopicViewSet.as_view({"get": "list", "post":"create"})),
    path("interest-profiles", InterestTopicProfileViewSet.as_view({"get": "list", "post":"create"})),
    path("interest-profiles/<int:pk>", InterestTopicProfileViewSet.as_view({"get": "retrieve"})),
    path("adept-profiles", AdeptTopicProfileViewSet.as_view({"get": "list", "post":"create"})),
    path("adept-profiles/<int:pk>", AdeptTopicProfileViewSet.as_view({"get": "retrieve"})),
]