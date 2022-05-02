from django.urls import path
from rest_framework import routers
from channeladmin.views import VideoUploadViewSet

router = routers.SimpleRouter()
router.register(r'upload', VideoUploadViewSet, basename='upload')

urlpatterns = [

]