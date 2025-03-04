from drf_yasg import openapi
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from exceptions.error_message import ErrorCodes
from exceptions.error_code import CustomAPIException
from api import models
from .serializers import (
    HomeBannerSerializer, CompanyCultureBannerSerializer, CompanyProgramsBannerSerializer,
    LeadershipTeamBannerSerializer, TeamMemberSerializer, EquipmentBannerSerializer,
    MaintenanceBannerSerializer, DarNewsBannerSerializer, DarNewsDetailSerializer,
    RefrigeratedDivisionBannerSerializer, FlatbedDivisionBannerSerializer,
    QualificationExpectationBannerSerializer, PayBenefitBannerSerializer,
    DriverTrainingProgramBannerSerializer, CDLHolderBannerSerializer,
    DriverAwardBannerSerializer, JobsSaidTransportBannerSerializer,
    JobsSaidTransportDetailSerializer, BenefitBannerSerializer,
    CompanyCultureSerializer, LeasePurchaseBannerSerializer, DarNewsSerializer,
    BenefitLeasingBannerSerializer, AboutUsSerializer, ContactSerializer,
    JobsSaidTransportSerializer, QuickLinkSerializer, JobsSaidTransportCategorySerializer,
    JobsSaidTransportLocationSerializer
)
from .repository.team_members_paginator import team_members_paginator
from .repository.dar_news_paginator import dar_news_paginator
from .repository.jobs_said_transport_paginator import jobs_said_transport_paginator
from django.db.models import Q


class MainViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: HomeBannerSerializer()},
        tags=['HomeBanner'],
    )
    def homepage(self, request):
        result = models.HomeBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': HomeBannerSerializer(result, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: CompanyCultureBannerSerializer()},
        tags=['CompanyCulture'],
    )
    def company_culture(self, request):
        data = models.CompanyCultureBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': CompanyCultureBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: CompanyProgramsBannerSerializer()},
        tags=['CompanyPrograms']
    )
    def company_programs(self, request):
        data = models.CompanyProgramsBanner.objects.order_by('-created_at').first()
        return Response(
            data={'result': CompanyProgramsBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: LeadershipTeamBannerSerializer()},
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
        responses={200: TeamMemberSerializer()},
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
        responses={200: TeamMemberSerializer()},
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
        responses={200: EquipmentBannerSerializer()},
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
        responses={200: MaintenanceBannerSerializer()},
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
        responses={200: DarNewsBannerSerializer()},
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
        responses={200: DarNewsSerializer()},
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
        responses={200: DarNewsDetailSerializer()},
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
        responses={200: RefrigeratedDivisionBannerSerializer()},
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
        responses={200: FlatbedDivisionBannerSerializer()},
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
        responses={200: QualificationExpectationBannerSerializer()},
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

    @swagger_auto_schema(
        responses={200: PayBenefitBannerSerializer()},
        tags=['PayBenefit']
    )
    def pay_benefit_banner(self, request):
        data = models.PayBenefitBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': PayBenefitBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: DriverTrainingProgramBannerSerializer()},
        tags=['DriverTrainingProgram']
    )
    def driver_training_program_banner(self, request):
        data = models.DriverTrainingProgramBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': DriverTrainingProgramBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: CDLHolderBannerSerializer()},
        tags=['CDLHolders']
    )
    def cdl_holder_banner(self, request):
        data = models.CDLHolderBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': CDLHolderBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: DriverAwardBannerSerializer()},
        tags=['DriverAwards']
    )
    def driver_award_banner(self, request):
        data = models.DriverAwardBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': DriverAwardBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: JobsSaidTransportBannerSerializer()},
        tags=['JobSaidTransport']
    )
    def jobs_said_transport_banner(self, request):
        data = models.JobsSaidTransportBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': JobsSaidTransportBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='page', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page number'),
            openapi.Parameter(
                name='page_size', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Page size number'),
            openapi.Parameter(
                name='q', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Search query'),
            openapi.Parameter(
                name='category', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Category id number'),
            openapi.Parameter(
                name='location', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='Location id number')
        ],
        responses={200: JobsSaidTransportSerializer()},
        tags=['JobSaidTransport']
    )
    def jobs_said_transport(self, request):
        page_size = request.query_params.get('page_size') or 10
        page = request.query_params.get('page') or 1
        q = request.query_params.get('q') or ''
        category = request.query_params.get('category')
        location = request.query_params.get('location')
        filter_ = Q()
        if q:
            filter_ &= Q(Q(name__icontains=q) | Q(description__icontains=q))

        if str(category).isdigit():
            filter_ &= Q(category_id=int(category))

        if str(location).isdigit():
            filter_ &= Q(location_id=int(location))

        items = models.JobsSaidTransport.objects.filter(filter_).order_by('-created_at')
        result = jobs_said_transport_paginator(items, context={'request': request}, page=page, page_size=page_size)
        return Response(data={'result': result, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: JobsSaidTransportDetailSerializer()},
        tags=['JobSaidTransport']
    )
    def jobs_said_transport_detail(self, request, pk):
        data = models.JobsSaidTransport.objects.filter(id=pk).first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': JobsSaidTransportDetailSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: JobsSaidTransportCategorySerializer()},
        tags=['JobSaidTransport']
    )
    def jobs_said_transport_category(self, request):
        category = models.JobsSaidTransportCategory.objects.all()
        serializer = JobsSaidTransportCategorySerializer(category, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: JobsSaidTransportLocationSerializer()},
        tags=['JobSaidTransport']
    )
    def jobs_said_transport_location(self, request):
        location = models.JobsSaidTransportLocation.objects.all()
        serializer = JobsSaidTransportLocationSerializer(location, many=True)
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: BenefitBannerSerializer()},
        tags=['Benefit']
    )
    def benefit_banner(self, request):
        data = models.BenefitBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': BenefitBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: CompanyCultureSerializer()},
        tags=['CompanyCultureTwo']
    )
    def company_culture_two(self, request):
        data = models.CompanyCulture.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)

        return Response(
            data={'result': CompanyCultureSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: LeasePurchaseBannerSerializer()},
        tags=['LeasePurchase']
    )
    def lease_purchase_banner(self, request):
        data = models.LeasePurchaseBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': LeasePurchaseBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: BenefitLeasingBannerSerializer()},
        tags=['BenefitLeasing']
    )
    def benefit_leasing_banner(self, request):
        data = models.BenefitLeasingBanner.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': BenefitLeasingBannerSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: AboutUsSerializer()},
        tags=['AboutUs']
    )
    def about_us(self, request):
        data = models.AboutUs.objects.order_by('-created_at').first()
        if not data:
            raise CustomAPIException(ErrorCodes.NOT_FOUND)
        return Response(
            data={'result': AboutUsSerializer(data, context={'request': request}).data, 'ok': True},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={200: ContactSerializer()},
        tags=['Contact']
    )
    def contact(self, request):
        serializer = ContactSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomAPIException(ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: QuickLinkSerializer()},
        tags=['QuickLink']
    )
    def quick_link(self, request):
        quick_link = models.QuickLink.objects.order_by('-created_at').first()
        serializer = QuickLinkSerializer(quick_link, context={'request': request})
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_200_OK)
