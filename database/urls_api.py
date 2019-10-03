from django.urls import path

from database import views
from django.conf.urls import url, include
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from database import views

app_name = 'database-api'

router = routers.DefaultRouter()
router.register(r'service', views.ServiceViewSet)
router.register(r'tool', views.ToolViewSet)
router.register(r'database', views.DatabaseViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'formation', views.FormationViewSet)
router.register(r'training_material', views.Training_materialViewSet)
router.register(r'platform', views.PlatformViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
