from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer
from django.urls import path, include
from rest_framework.authtoken import views

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from .views import BugViewSet, UserViewSet


router = routers.SimpleRouter()
router.register("bug", BugViewSet)
router.register("user", UserViewSet)



schema_view = get_schema_view(
    title="Bug Tracker",
    renderer_classes=[JSONOpenAPIRenderer],
)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth-token/", views.obtain_auth_token),
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
