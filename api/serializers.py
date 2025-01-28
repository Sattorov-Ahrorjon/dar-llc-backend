from rest_framework import serializers
import models


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_video')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['statistic'] = HomeStatisticSerializer(
            models.HomeStatistic.objects.filter('-created_at').first(), context=self.context
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
            models.Equipment.objects.filter('-created_at'), many=True, context=self.context
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
