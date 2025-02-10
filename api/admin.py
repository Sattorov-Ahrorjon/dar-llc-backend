from django.contrib import admin
from api import models


@admin.register(models.HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_text')
    list_display_links = ('id', 'banner_text')


@admin.register(models.HomeStatistic)
class HomeStatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.CompanyCultureBanner)
class CompanyCultureBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')


@admin.register(models.CompanyProgramsBanner)
class CompanyProgramsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.LeadershipTeamBanner)
class LeadershipTeamBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_desc')
    list_display_links = ('id', 'short_desc')


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'is_published')
    list_display_links = ('id', 'full_name')


@admin.register(models.EquipmentBanner)
class EquipmentBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)


@admin.register(models.MaintenanceBanner)
class MaintenanceBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')


@admin.register(models.MaintenanceBenefit)
class MaintenanceBenefitAdmin(admin.ModelAdmin):
    list_display = ('id', 'about', 'is_top')
    list_display_links = ('id', 'about')


@admin.register(models.MaintenanceBenefitImage)
class MaintenanceBenefitImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_link', 'image')
    list_display_links = ('id', 'item_link')


@admin.register(models.DarNewsBanner)
class DarNewsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.DarNews)
class DarNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_definition')
    list_display_links = ('id', 'title')


@admin.register(models.ApartAdvantage)
class ApartAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_text')
    list_display_links = ('id', 'short_text')


@admin.register(models.RefrigeratedDivisionBanner)
class RefrigeratedDivisionBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')


@admin.register(models.FlatbedDivisionBanner)
class FlatbedDivisionBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.QualificationExpectationBanner)
class QualificationExpectationBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.QualificationExpectation)
class QualificationExpectationAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'short_descr')
    list_display_links = ('id', 'category')


@admin.register(models.QualificationExpectationImage)
class QualificationExpectationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id', 'category')


@admin.register(models.PayBenefitBanner)
class PayBenefitBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_desc')
    list_display_links = ('id', 'short_desc')


@admin.register(models.PayBenefitItem)
class PayBenefitItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title',)


@admin.register(models.PayBenefitTable)
class PayBenefitTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_type', 'dry_van', 'team_bonus')
    list_display_links = ('id', 'position_type', 'team_bonus')


@admin.register(models.DriverTrainingProgramBanner)
class DriverTrainingProgramBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')


@admin.register(models.CDLHolderBanner)
class CDLHolderBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.CDLHolderAdvantage)
class CDLHolderAdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_definition')
    list_display_links = ('id', 'title',)


@admin.register(models.DriverAwardBanner)
class DriverAwardBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_text')
    list_display_links = ('id', 'banner_text')


@admin.register(models.TransportLeadershipElite)
class TransportLeadershipEliteAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.SafetyChampionAwards)
class SafetyChampionAwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_desc')
    list_display_links = ('id', 'short_desc')


@admin.register(models.JobsSaidTransportBanner)
class JobsSaidTransportBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_text')
    list_display_links = ('id', 'banner_text')


@admin.register(models.JobsSaidTransport)
class JobsSaidTransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_desc')
    list_display_links = ('id', 'name',)


@admin.register(models.KeyResponsibility)
class KeyResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'text')
    list_display_links = ('id', 'job',)


@admin.register(models.BenefitBanner)
class BenefitBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.HolidayObserver)
class HolidayObserverAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_text')
    list_display_links = ('id', 'banner_text')


@admin.register(models.AdditionalBenefits)
class AdditionalBenefitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_description')
    list_display_links = ('id', 'short_description')


@admin.register(models.CompanyCulture)
class CompanyCultureAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.CompanyCultureItem)
class CompanyCultureItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_definition')
    list_display_links = ('id', 'title')


@admin.register(models.LeasePurchaseBanner)
class LeasePurchaseBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_desc')
    list_display_links = ('id', 'short_desc')


@admin.register(models.StandardLeaseDefinition)
class StandardLeaseDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.StandardLeaseItem)
class StandardLeaseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_desc')
    list_display_links = ('id', 'title')


@admin.register(models.LeasePurchaseDefinition)
class LeasePurchaseDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_desc')
    list_display_links = ('id', 'short_desc')


@admin.register(models.LeasePurchaseItem)
class LeasePurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_desc')
    list_display_links = ('id', 'title',)


@admin.register(models.LeasePurchaseImage)
class LeasePurchaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'obj_link')
    list_display_links = ('id', 'obj_link')


@admin.register(models.BenefitLeasingBanner)
class BenefitLeasingBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_desc')
    list_display_links = ('id', 'banner_desc')


@admin.register(models.BenefitLeasingInformation)
class BenefitLeasingInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.BenefitLeasingInformationItem)
class BenefitLeasingInformationItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_definition')
    list_display_links = ('id', 'short_definition')


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram', 'instagram', 'facebook', 'linkedin')
    list_display_links = ('id', 'telegram')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(models.TrainingProgramCategory)
class TrainingProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
