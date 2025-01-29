from drf_yasg import openapi
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from exceptions.error_message import ErrorCodes
from exceptions.error_code import CustomAPIException
import models
from .serializers import (
    HomeBannerSerializer, CompanyCultureBannerSerializer, CompanyProgramsBannerSerializer,
    LeadershipTeamBannerSerializer, TeamMemberSerializer, EquipmentBannerSerializer,
    MaintenanceBannerSerializer, DarNewsBannerSerializer, DarNewsDetailSerializer,
    RefrigeratedDivisionBannerSerializer, FlatbedDivisionBannerSerializer,
    QualificationExpectationBannerSerializer
)
from .repository.team_members_paginator import team_members_paginator
from .repository.dar_news_paginator import dar_news_paginator


class MainViewSet(ViewSet):
    @swagger_auto_schema(
        tags=['HomeBanner'],
    )
    def homepage(self, request):
        result = models.HomeBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': HomeBannerSerializer(result, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['CompanyCulture'],
    )
    def company_culture(self, request):
        data = models.CompanyCultureBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': CompanyCultureBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['CompanyPrograms']
    )
    def company_programs(self, request):
        data = models.CompanyProgramsBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': CompanyProgramsBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['LeadershipTeam']
    )
    def leadership_team(self, request):
        data = models.LeadershipTeamBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': LeadershipTeamBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page number'),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page size'),
        ],
        tags=['LeadershipTeam']
    )
    def leadership_teams_members(self, request):
        page = request.query_params.get('page') or 1
        page_size = request.query_params.get('page_size') or 10

        if (str(page).isdigit() and int(page) < 1) or (str(page_size).isdigit() and int(page_size) < 1):
            raise CustomAPIException(
                ErrorCodes.INVALID_INPUT, message='Page and Pagesize must be greater than or equal to 1.')

        data = models.TeamMember.objects.filter(is_published=True).order_by('-created_at')
        result = team_members_paginator(data, context={'request': request}, page=page, page_size=page_size)
        return Response(data={'result': result, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['LeadershipTeam'],
    )
    def leadership_teams_member(self, request, pk):
        result = models.TeamMember.objects.filter(id=pk, is_published=True).first()
        if not result:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': TeamMemberSerializer(result, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['Equipment']
    )
    def equipment(self, request):
        data = models.EquipmentBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': EquipmentBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['FleetMaintenance']
    )
    def fleet_maintenance(self, request):
        data = models.MaintenanceBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': MaintenanceBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['DarNews']
    )
    def dar_news_banner(self, request):
        result = models.DarNewsBanner.objects.order_by('-created_at').first()
        if not result:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': DarNewsBannerSerializer(result, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page number'),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page size number'),
        ],
        tags=['DarNews']
    )
    def dar_news_list(self, request):
        page_size = request.query_params.get('page_size') or 10
        page = request.query_params.get('page') or 1

        if (str(page).isdigit() and int(page) < 1) or (str(page_size).isdigit() and int(page_size) < 1):
            raise CustomAPIException(
                ErrorCodes.INVALID_INPUT, message='Page and Pagesize must be greater than or equal to 1.')
        news = models.DarNews.objects.order_by('-created_at')
        result = dar_news_paginator(news, context={'request': request}, page=page, page_size=page_size)
        return Response(data={'result': result, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['DarNews']
    )
    def dar_news_detail(self, request, pk):
        data = models.DarNews.objects.filter(id=pk).first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': DarNewsDetailSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['RefrigeratedDivision'],
    )
    def refrigerated_division(self, request):
        data = models.RefrigeratedDivisionBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': RefrigeratedDivisionBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['FlatbedDivision']
    )
    def flatbed_division(self, request):
        data = models.FlatbedDivisionBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': FlatbedDivisionBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=['QualificationExpectation']
    )
    def qualification_expectation(self, request):
        data = models.QualificationExpectationBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={
                'result': QualificationExpectationBannerSerializer(data, context={'request': request}).data,
                'ok': True},
            status=status.HTTP_200_OK
        )
