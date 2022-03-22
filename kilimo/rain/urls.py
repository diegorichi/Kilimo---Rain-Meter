# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import GroundViewSet, RainViewSet
router = routers.DefaultRouter(trailing_slash = False)
router.register(r'rains', RainViewSet)
router.register(r'grounds', GroundViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
