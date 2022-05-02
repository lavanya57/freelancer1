import imp
from channeladmin.models import VideoUpload
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


class VideoUploadViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = VideoUpload.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        return Response("<h1> hi welcome to my new project </h1>")

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes] 