from rest_framework import serializers
import models


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_video')


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


class TeamMemberSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamMember
        fields = (
            'id', 'full_name', 'position', 'description', 'image', 'is_published'
        )


class EquipmentBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EquipmentBanner
        fields = ('id', 'banner_title', 'banner_description', 'banner_image')


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


class ApartAdvantageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApartAdvantageCategory
        fields = ('id', 'title')


class ApartAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApartAdvantage
        fields = ('id', 'advantage_category', 'advantage_text')


class OurRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurRequirement
        fields = ('id', 'title')
