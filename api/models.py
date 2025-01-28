from django.db import models
from django.core.validators import FileExtensionValidator

QualificationCategory = (
    (1, 'Minimum Requirements'),
    (2, 'Documents'),
    (3, 'Criminal History'),
    (4, 'Medical Requirements'),
)

AboutPayBenefitCategory = (
    (1, 'Company Driver Benefits'),
    (2, 'Independent Contractor Benefits')
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HomeBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_video = models.FileField(
        upload_to='banner/home/', validators=[FileExtensionValidator(['mp4'])])

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.banner_title


class HomeStatistic(BaseModel):
    description = models.TextField()
    satisfaction = models.FloatField(default=0)
    active_clients = models.PositiveIntegerField(default=0)
    support_availability = models.CharField(max_length=5)
    loads_delivered = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.description


class CompanyCultureBanner(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/culture/', validators=[FileExtensionValidator(['jpg'])])
    information_image = models.FileField(
        upload_to='about/culture/', validators=[FileExtensionValidator(['jpg'])])
    information_description = models.TextField()


class CompanyProgramsBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/programs/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_image = models.FileField(
        upload_to='about/programs/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()


class LeadershipTeamBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/teams/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()


class TeamMember(BaseModel):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='teams/', validators=[FileExtensionValidator(['jpg'])])
    is_published = models.BooleanField(default=False)


class EquipmentBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/equipment/', validators=[FileExtensionValidator(['jpg'])])


class Equipment(BaseModel):
    title = models.CharField(max_length=150)
    model = models.CharField(max_length=250)
    engine = models.CharField(max_length=250)
    transmission = models.CharField(max_length=250)
    sleeper = models.CharField(max_length=250)
    inverter = models.CharField(max_length=250)
    apu = models.CharField(max_length=250)
    image = models.FileField(
        upload_to='equipment/', validators=[FileExtensionValidator(['jpg'])])


class MaintenanceBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_video = models.FileField(
        upload_to='banner/maintenance/', validators=[FileExtensionValidator(['mp4'])]
    )
    information_description = models.TextField()


class MaintenanceBenefitText(BaseModel):
    description = models.TextField()


class MaintenanceBenefit(models.Model):
    about = models.CharField(max_length=150)
    is_top = models.BooleanField(default=False)


class MaintenanceBenefitImage(BaseModel):
    image = models.FileField(
        upload_to='maintenance/', validators=[FileExtensionValidator(['jpg'])]
    )


class DarNewsBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/news/', validators=[FileExtensionValidator(['jpg'])]
    )


class DarNews(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='news/', validators=[FileExtensionValidator(['jpg'])]
    )


class ApartAdvantageCategory(BaseModel):
    title = models.CharField(max_length=150)


class ApartAdvantage(BaseModel):
    advantage_category = models.ForeignKey(ApartAdvantageCategory, on_delete=models.CASCADE)
    advantage_text = models.CharField(max_length=250)


class OurRequirement(BaseModel):
    title = models.CharField(max_length=150)


class RefrigeratedDivisionBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/refrigerated/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='refrigerated/', validators=[FileExtensionValidator(['jpg'])]
    )


class FlatbedDivisionBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/flatbed/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='flatbed/', validators=[FileExtensionValidator(['jpg'])]
    )


class QualificationExpectationBanner(models.Model):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/qualification/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='qualification/', validators=[FileExtensionValidator(['jpg'])]
    )


class QualificationExpectation(BaseModel):
    category = models.IntegerField(choices=QualificationCategory, default=1)
    instance = models.CharField(max_length=150)


class PayBenefitBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )


class AboutPayBenefit(BaseModel):
    category = models.IntegerField(choices=AboutPayBenefitCategory, default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='about_pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )


class DriverTrainingProgramBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/training_program/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()


class TrainingProgramCategory(BaseModel):
    title = models.CharField(max_length=150)


class TrainingProgram(BaseModel):
    category = models.ForeignKey(TrainingProgramCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)


class CDLHolderBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/cdl_holders/', validators=[FileExtensionValidator(['jpg'])]
    )


class CDLHolderAdvantage(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='cdl_holders/advantage/', validators=[FileExtensionValidator(['jpg'])]
    )


class DriverAwardBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/driver_award/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='driver_award/', validators=[FileExtensionValidator(['jpg'])]
    )


class TransportLeadershipElite(BaseModel):
    description = models.TextField()


class TransportLeadershipEliteStar(BaseModel):
    time = models.CharField(max_length=150)
    definition = models.TextField()


class SafetyChampionAwards(BaseModel):
    description = models.TextField()


class SafetyChampionAwardsStar(BaseModel):
    time = models.CharField(max_length=150)
    definition = models.TextField()


class JobsSaidTransportBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/jobs_said_transport/', validators=[FileExtensionValidator(['jpg'])]
    )


class JobsSaidTransport(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(
        upload_to='jobs_said_transport/', validators=[FileExtensionValidator(['jpg'])]
    )


class KeyResponsibility(BaseModel):
    job = models.ForeignKey(JobsSaidTransport, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)


class BenefitBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/benefit/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()


class HolidayObserver(BaseModel):
    description = models.TextField()


class Holiday(BaseModel):
    name = models.CharField(max_length=90)
    icon_image = models.FileField(
        upload_to='holiday/', validators=[FileExtensionValidator(['jpg'])]
    )


class AdditionalBenefits(BaseModel):
    description = models.TextField()


class AdditionalBenefitsItem(BaseModel):
    name = models.CharField(max_length=90)
    icon_image = models.FileField(
        upload_to='additional_benefits/', validators=[FileExtensionValidator(['jpg'])]
    )


class CompanyCulture(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/company_culture/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='company_culture/', validators=[FileExtensionValidator(['jpg'])]
    )


class CompanyCultureItem(BaseModel):
    title = models.CharField(max_length=90)
    definition = models.TextField()


class LeasePurchaseBanner(BaseModel):
    banner_title = models.CharField(max_length=150)
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/lease_purchase/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='lease_purchase/', validators=[FileExtensionValidator(['jpg'])]
    )


class StandardLeaseDefinition(BaseModel):
    description = models.TextField()


class StandardLeaseCategory(BaseModel):
    title = models.CharField(max_length=90)


class StandardLeaseItem(BaseModel):
    category = models.ForeignKey(StandardLeaseCategory, on_delete=models.CASCADE)
    definition = models.CharField(max_length=150)


class LeasePurchaseDefinition(BaseModel):
    description = models.TextField()


class LeasePurchaseCategory(BaseModel):
    title = models.CharField(max_length=90)


class LeasePurchaseItem(BaseModel):
    category = models.ForeignKey(LeasePurchaseCategory, on_delete=models.CASCADE)
    definition = models.CharField(max_length=150)


class BenefitLeasingBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/benefits_leasing/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='benefits_leasing/', validators=[FileExtensionValidator(['jpg'])]
    )


class BenefitLeasingInformation(BaseModel):
    description = models.TextField()


class BenefitLeasingInformationItem(BaseModel):
    definition = models.CharField(max_length=150)


class BenefitLeasingStar(BaseModel):
    definition = models.CharField(max_length=100)


class AboutUs(BaseModel):
    telegram = models.CharField(max_length=40, blank=True, null=True)
    instagram = models.CharField(max_length=40, blank=True, null=True)
    facebook = models.CharField(max_length=40, blank=True, null=True)
    linkedin = models.CharField(max_length=40, blank=True, null=True)


class Contact(BaseModel):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
