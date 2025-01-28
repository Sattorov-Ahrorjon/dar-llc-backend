from drf_yasg import openapi
from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from exceptions.error_message import ErrorCodes
from exceptions.error_code import CustomAPIException
from .serializers import HomeBannerSerializer
import models


class MainViewSet(ViewSet):
    @swagger_auto_schema(
        tags=['HomeBanner'],
    )
    def homepage(self, request):
        result = models.HomeBanner.objects.order_by('-created_at').first()
        return Response(
            data={
                'result': HomeBannerSerializer(result, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )
