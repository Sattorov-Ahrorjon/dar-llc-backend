from rest_framework import serializers
import models


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_video')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['statistic'] = HomeStatisticSerializer(
            models.HomeStatistic.objects.first(), context=self.context
        ).data
        return data


class HomeStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeStatistic
        fields = ('id', 'description', 'satisfaction', 'active_clients', 'support_availability', 'loads_delivered')


class CompanyCultureBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyCultureBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_image',
            'information_description'
        )


class CompanyProgramsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyProgramsBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description',
            'information_image'
        )


class LeadershipTeamBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeadershipTeamBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description'
        )


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMember
        fields = (
            'id', 'full_name', 'position', 'description', 'image', 'is_published'
        )


class EquipmentBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EquipmentBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = EquipmentSerializer(
            models.Equipment.objects.all(), many=True, context=self.context
        ).data
        return data


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = (
            'id', 'title', 'model', 'engine', 'transmission', 'sleeper', 'inverter', 'apu', 'image'
        )


class MaintenanceBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_video', 'information_description'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['benefits'] = {
            'benefits_top_items': MaintenanceBenefitSerializer(
                models.MaintenanceBenefit.objects.filter('-created_at', is_top=True),
                many=True, context=self.context
            ).data,
            'team_images': MaintenanceBenefitImageSerializer(
                models.MaintenanceBenefitImage.objects.filter('-created_at'), many=True, context=self.context
            ).data,
            'benefits_text': MaintenanceBenefitTextSerializer(
                models.MaintenanceBenefitText.objects.filter('-created_at').first(), context=self.context
            ).data,
            'benefits_items': MaintenanceBenefitSerializer(
                models.MaintenanceBenefit.objects.filter('-created_at', is_top=False),
                many=True, context=self.context
            ).data,
        }


class MaintenanceBenefitTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceBenefitText
        fields = ('id', 'description')


class MaintenanceBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceBenefit
        fields = ('id', 'about', 'is_top')


class MaintenanceBenefitImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceBenefitImage
        fields = ('id', 'image')


class DarNewsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DarNewsBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image')


class DarNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DarNews
        fields = ('id', 'title', 'description', 'image')


class DarNewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DarNews
        fields = ('id', 'title', 'description', 'image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional_news'] = DarNewsSerializer(
            models.DarNews.objects.filter('-created_at'), many=True, context=self.context
        ).data

        data['apart_advantage'] = ApartAdvantageSerializer(
            models.ApartAdvantage.objects.filter('-created_at'), many=True, context=self.context
        ).data

        data['our_requirements'] = OurRequirementSerializer(
            models.OurRequirement.objects.filter('-created_at'), many=True, context=self.context
        ).data

        return data


class ApartAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApartAdvantage
        fields = ('id', 'advantage_category', 'advantage_text')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['advantage_category'] = getattr(instance.advantage_category, 'title', 'Not category')
        return data


class OurRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurRequirement
        fields = ('id', 'title')


class RefrigeratedDivisionBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RefrigeratedDivisionBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )


class FlatbedDivisionBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlatbedDivisionBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )


class QualificationExpectationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QualificationExpectationBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = QualificationExpectationSerializer(
            models.QualificationExpectation.objects.filter('-created_at'), many=True, context=self.context
        ).data
        return data


class QualificationExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QualificationExpectation
        fields = ('id', 'category', 'instance')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category_name'] = dict(models.QualificationCategory).get(instance.category)
        return data


class PayBenefitBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PayBenefitBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['company_driver_benefits'] = AboutPayBenefitSerializer(
            models.AboutPayBenefit.objects.filter(category=1).order_by('-created_at'), many=True, context=self.context
        ).data
        data['independent_contractor_benefits'] = AboutPayBenefitSerializer(
            models.AboutPayBenefit.objects.filter(category=2).order_by('-created_at'), many=True, context=self.context
        ).data
        return data


class AboutPayBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutPayBenefit
        fields = ('id', 'category', 'title', 'description', 'icon_image')


class DriverTrainingProgramBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DriverTrainingProgramBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image', 'information_description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        result = []
        category = models.TrainingProgramCategory.objects.order_by('-created_at')
        for cat in category:
            cat_items = TrainingProgramSerializer(
                models.TrainingProgram.objects.filter(category=cat).order_by('created_at'),
                many=True, context=self.context
            ).data
            result.append(
                {
                    'category': cat.title,
                    'items': cat_items
                }
            )

        data['training_program'] = result
        return data


class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrainingProgram
        fields = ('id', 'category', 'title')


class CDLHolderBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CDLHolderBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['advantage'] = CDLHolderAdvantageSerializer(
            models.CDLHolderAdvantage.objects.all(), many=True, context=self.context
        ).data
        return data


class CDLHolderAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CDLHolderAdvantage
        fields = ('id', 'title', 'description', 'icon_image')


class DriverAwardBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DriverAwardBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = {
            'transport_leadership_elite': {
                'description': DriverAwardBodyDescriptionSerializer(
                    models.TransportLeadershipElite.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'items': DriverAwardBodyStarSerializer(
                    models.TransportLeadershipEliteStar.objects.all(), many=True, context=self.context
                ).data
            },
            'safety_champion_awards': {
                'description': DriverAwardBodyDescriptionSerializer(
                    models.SafetyChampionAwards.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'items': DriverAwardBodyStarSerializer(
                    models.SafetyChampionAwardsStar.objects.all(), many=True, context=self.context
                ).data
            }
        }


class DriverAwardBodyDescriptionSerializer(serializers.Serializer):
    description = serializers.CharField()


class DriverAwardBodyStarSerializer(serializers.Serializer):
    time = serializers.CharField()
    definition = serializers.CharField()


class JobsSaidTransportBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobsSaidTransportBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image')


class JobsSaidTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobsSaidTransport
        fields = ('id', 'name', 'description', 'image')


class JobsSaidTransportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobsSaidTransport
        fields = ('id', 'name', 'description', 'image')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['key_responsibility'] = KeyResponsibilitySerializer(
            instance.job_said_transport, many=True, context=self.context
        ).data
        return data


class KeyResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KeyResponsibility
        fields = ('id', 'job', 'text')


class BenefitBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BenefitBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image', 'information_description')

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['additional'] = {
            'holiday_observed': {
                'holiday_text': TextSerializer(
                    models.HolidayObserver.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'holiday_items': ItemSerializer(
                    models.HolidayObserverItem.objects.all(), many=True, context=self.context
                ).data
            },
            'additional_benefits': {
                'additional_text': TextSerializer(
                    models.AdditionalBenefits.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'additional_items': ItemSerializer(
                    models.AdditionalBenefitsItem.objects.all(), many=True, context=self.context
                ).data
            }
        }

        return data


class TextSerializer(serializers.Serializer):
    description = serializers.CharField()


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    icon_image = serializers.CharField()


class CompanyCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyCulture
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = CompanyCultureItemSerializer(
            models.CompanyCultureItem.objects.all(), many=True, context=self.context
        ).data
        return data


class CompanyCultureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyCultureItem
        fields = ('id', 'title', 'definition')


class LeasePurchaseBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeasePurchaseBanner
        fields = (
            'id', 'banner_title', 'banner_description', 'banner_image', 'information_description', 'information_image'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = {
            'standard_lease': {
                'description': TextSerializer(
                    models.StandardLeaseDefinition.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'items': LeasePurchaseItemSerializer(
                    models.StandardLeaseItem.objects.all(), many=True, context=self.context
                ).data
            },
            'lease_purchase': {
                'description': TextSerializer(
                    models.LeasePurchaseDefinition.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'items': LeasePurchaseItemSerializer(
                    models.LeasePurchaseItem.objects.all(), many=True, context=self.context
                ).data
            }
        }
        return data


class LeasePurchaseItemSerializer(serializers.Serializer):
    category = serializers.ReadOnlyField()
    definition = serializers.CharField()


class BenefitLeasingBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BenefitLeasingBanner
        fields = ('id', 'banner_image', 'banner_description', 'information_image', 'information_description')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['additional'] = {
            'benefit_leasing': {
                'description': TextSerializer(
                    models.BenefitLeasingInformation.objects.order_by('-created_at').first(), context=self.context
                ).data,
                'definition_items': BenefitDefinitionItemSerializer(
                    models.BenefitLeasingInformationItem.objects.all(), many=True, context=self.context
                ).data,
                'star_items': BenefitDefinitionItemSerializer(
                    models.BenefitLeasingStar.objects.all(), many=True, context=self.context
                ).data
            }
        }
        return data


class BenefitDefinitionItemSerializer(serializers.Serializer):
    definition = serializers.CharField()


class AboutUs(serializers.ModelSerializer):
    telegram = serializers.CharField()
    instagram = serializers.CharField()
    facebook = serializers.CharField()
    linkedin = serializers.CharField()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('id', 'full_name', 'phone_number')
