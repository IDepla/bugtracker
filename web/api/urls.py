from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer
from django.urls import path, include


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = routers.SimpleRouter()


schema_view = get_schema_view(
    title="Bug Tracker",
    renderer_classes=[JSONOpenAPIRenderer],
)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        f"api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
