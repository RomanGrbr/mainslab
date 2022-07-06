from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CheckViewSet, ClientsViewSet, UploadeViewSet

app_name = "api"

router = DefaultRouter()
router.register("uploade", UploadeViewSet, basename="uploade"),
router.register("clients", ClientsViewSet, basename="clients")
router.register("check", CheckViewSet, basename="check")

urlpatterns = [
    path('', include(router.urls)),
    path('', include("djoser.urls")),
]
