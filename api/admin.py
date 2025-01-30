from django.contrib import admin
from api import models


@admin.register(models.HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.HomeStatistic)
class HomeStatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.CompanyCultureBanner)
class CompanyCultureBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.CompanyProgramsBanner)
class CompanyProgramsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.LeadershipTeamBanner)
class LeadershipTeamBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position')


@admin.register(models.EquipmentBanner)
class EquipmentBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)


@admin.register(models.MaintenanceBanner)
class MaintenanceBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.MaintenanceBenefitText)
class MaintenanceBenefitTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.MaintenanceBenefit)
class MaintenanceBenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'about')


@admin.register(models.MaintenanceBenefitImage)
class MaintenanceBenefitImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(models.DarNewsBanner)
class DarNewsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.DarNews)
class DarNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.ApartAdvantage)
class ApartAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'advantage_category', 'advantage_text')


@admin.register(models.OurRequirement)
class OurRequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.RefrigeratedDivisionBanner)
class RefrigeratedDivisionBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.FlatbedDivisionBanner)
class FlatbedDivisionBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.QualificationExpectationBanner)
class QualificationExpectationBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.QualificationExpectation)
class QualificationExpectationAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'instance')


@admin.register(models.PayBenefitBanner)
class PayBenefitBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.AboutPayBenefit)
class AboutPayBenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(models.DriverTrainingProgramBanner)
class DriverTrainingProgramBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(models.CDLHolderBanner)
class CDLHolderBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.CDLHolderAdvantage)
class CDLHolderAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(models.DriverAwardBanner)
class DriverAwardBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.TransportLeadershipElite)
class TransportLeadershipEliteAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.TransportLeadershipEliteStar)
class TransportLeadershipEliteStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'definition')


@admin.register(models.SafetyChampionAwards)
class SafetyChampionAwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.SafetyChampionAwardsStar)
class SafetyChampionAwardsStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'definition')


@admin.register(models.JobsSaidTransportBanner)
class JobsSaidTransportBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.JobsSaidTransport)
class JobsSaidTransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(models.KeyResponsibility)
class KeyResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('job', 'text')


@admin.register(models.BenefitBanner)
class BenefitBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.HolidayObserver)
class HolidayObserverAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.HolidayObserverItem)
class HolidayObserverItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.AdditionalBenefits)
class AdditionalBenefitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.AdditionalBenefitsItem)
class AdditionalBenefitsItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.CompanyCulture)
class CompanyCultureAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.CompanyCultureItem)
class CompanyCultureItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'definition')


@admin.register(models.LeasePurchaseBanner)
class LeasePurchaseBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.StandardLeaseDefinition)
class StandardLeaseDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.StandardLeaseItem)
class StandardLeaseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'definition')


@admin.register(models.LeasePurchaseDefinition)
class LeasePurchaseDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.LeasePurchaseItem)
class LeasePurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'definition')


@admin.register(models.BenefitLeasingBanner)
class BenefitLeasingBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_description')


@admin.register(models.BenefitLeasingInformation)
class BenefitLeasingInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(models.BenefitLeasingInformationItem)
class BenefitLeasingInformationItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'definition')


@admin.register(models.BenefitLeasingStar)
class BenefitLeasingStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'definition')


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram', 'instagram', 'facebook', 'linkedin')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(models.LeasePurchaseCategory)
class LeasePurchaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.JobsSaidTransport)
class JobsSaidTransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.TrainingProgramCategory)
class TrainingProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.ApartAdvantageCategory)
class ApartAdvantageCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
