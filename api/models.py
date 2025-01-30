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
    banner_description = models.TextField()
    banner_video = models.FileField(
        upload_to='banner/home/', validators=[FileExtensionValidator(['mp4'])])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Home banner'
        verbose_name_plural = 'Home banners'

    def __str__(self):
        return self.banner_description


class HomeStatistic(BaseModel):
    description = models.TextField()
    satisfaction = models.FloatField(default=0)
    active_clients = models.PositiveIntegerField(default=0)
    support_availability = models.CharField(max_length=5)
    loads_delivered = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Home statistic'
        verbose_name_plural = 'Home statistics'

    def __str__(self):
        return self.description


class CompanyCultureBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/culture/', validators=[FileExtensionValidator(['jpg'])])
    information_image = models.FileField(
        upload_to='about/culture/', validators=[FileExtensionValidator(['jpg'])])
    information_description = models.TextField()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Company culture banner'
        verbose_name_plural = 'Company culture banners'

    def __str__(self):
        return self.banner_description


class CompanyProgramsBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/programs/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_image = models.FileField(
        upload_to='about/programs/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Company programs banner'
        verbose_name_plural = 'Company programs banners'

    def __str__(self):
        return self.banner_description


class LeadershipTeamBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/teams/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Leadership team banner'
        verbose_name_plural = 'Leadership team banners'

    def __str__(self):
        return self.banner_description


class TeamMember(BaseModel):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='teams/', validators=[FileExtensionValidator(['jpg'])])
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team members'

    def __str__(self):
        return self.full_name


class EquipmentBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/equipment/', validators=[FileExtensionValidator(['jpg'])])

    class Meta:
        verbose_name = 'Equipment banner'
        verbose_name_plural = 'Equipment banners'

    def __str__(self):
        return self.banner_description


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

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return self.title


class MaintenanceBanner(BaseModel):
    banner_description = models.TextField()
    banner_video = models.FileField(
        upload_to='banner/maintenance/', validators=[FileExtensionValidator(['mp4'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Maintenance banner'
        verbose_name_plural = 'Maintenance banners'

    def __str__(self):
        return self.banner_description


class MaintenanceBenefitText(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Maintenance benefit'
        verbose_name_plural = 'Maintenance benefits'

    def __str__(self):
        return self.description


class MaintenanceBenefit(models.Model):
    about = models.CharField(max_length=150)
    is_top = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Maintenance benefit'
        verbose_name_plural = 'Maintenance benefits'

    def __str__(self):
        return self.about


class MaintenanceBenefitImage(BaseModel):
    image = models.FileField(
        upload_to='maintenance/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Maintenance benefit'
        verbose_name_plural = 'Maintenance benefits'

    def __str__(self):
        return str(self.id)


class DarNewsBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/news/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Dar news banner'
        verbose_name_plural = 'Dar news banners'

    def __str__(self):
        return self.banner_description


class DarNews(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='news/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Dar news'
        verbose_name_plural = 'Dar news'

    def __str__(self):
        return self.title


class ApartAdvantageCategory(BaseModel):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Apart advantage category'
        verbose_name_plural = 'Apart advantage category'


class ApartAdvantage(BaseModel):
    advantage_category = models.ForeignKey(ApartAdvantageCategory, on_delete=models.CASCADE)
    advantage_text = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Apart advantage'
        verbose_name_plural = 'Apart advantage'

    def __str__(self):
        return self.advantage_category.title


class OurRequirement(BaseModel):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Our requirement'
        verbose_name_plural = 'Our requirements'

    def __str__(self):
        return self.title


class RefrigeratedDivisionBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/refrigerated/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='refrigerated/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Refrigerated division banner'
        verbose_name_plural = 'Refrigerated division banners'

    def __str__(self):
        return self.banner_description


class FlatbedDivisionBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/flatbed/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='flatbed/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Flatbed division banner'
        verbose_name_plural = 'Flatbed division banners'

    def __str__(self):
        return self.banner_description


class QualificationExpectationBanner(models.Model):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/qualification/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='qualification/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Qualification expectation banner'
        verbose_name_plural = 'Qualification expectation banners'

    def __str__(self):
        return self.banner_description


class QualificationExpectation(BaseModel):
    category = models.IntegerField(choices=QualificationCategory, default=1)
    instance = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Qualification expectation'
        verbose_name_plural = 'Qualification expectations'

    def __str__(self):
        return self.instance


class PayBenefitBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Pay benefit banner'
        verbose_name_plural = 'Pay benefits banner'

    def __str__(self):
        return self.banner_description


class AboutPayBenefit(BaseModel):
    category = models.IntegerField(choices=AboutPayBenefitCategory, default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='about_pay_benefit/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'About pay benefit'
        verbose_name_plural = 'About pay benefits'

    def __str__(self):
        return self.title


class DriverTrainingProgramBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/training_program/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Driver training program banner'
        verbose_name_plural = 'Driver training program banners'

    def __str__(self):
        return self.banner_description


class TrainingProgramCategory(BaseModel):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Training program category'
        verbose_name_plural = 'Training program categories'

    def __str__(self):
        return self.title


class TrainingProgram(BaseModel):
    category = models.ForeignKey(TrainingProgramCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Training program'
        verbose_name_plural = 'Training program'

    def __str__(self):
        return self.title


class CDLHolderBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/cdl_holders/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'CDL holder banner'
        verbose_name_plural = 'CDL holder banners'

    def __str__(self):
        return self.banner_description


class CDLHolderAdvantage(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='cdl_holders/advantage/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'CDL holder advantage'
        verbose_name_plural = 'CDL holder advantage'

    def __str__(self):
        return self.title


class DriverAwardBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/driver_award/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='driver_award/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Driver award banner'
        verbose_name_plural = 'Driver award banners'

    def __str__(self):
        return self.banner_description


class TransportLeadershipElite(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Transport leadership elite'
        verbose_name_plural = 'Transport leadership elites'

    def __str__(self):
        return self.description


class TransportLeadershipEliteStar(BaseModel):
    time = models.CharField(max_length=150)
    definition = models.TextField()

    class Meta:
        verbose_name = 'Transport leadership elite star'
        verbose_name_plural = 'Transport leadership elite stars'

    def __str__(self):
        return self.time


class SafetyChampionAwards(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Safety champion awards'
        verbose_name_plural = 'Safety champion awards'

    def __str__(self):
        return self.description


class SafetyChampionAwardsStar(BaseModel):
    time = models.CharField(max_length=150)
    definition = models.TextField()

    class Meta:
        verbose_name = 'Safety champion awards star'
        verbose_name_plural = 'Safety champion awards stars'

    def __str__(self):
        return self.time


class JobsSaidTransportBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/jobs_said_transport/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Jobs said transport banner'
        verbose_name_plural = 'Jobs said transport banners'

    def __str__(self):
        return self.banner_description


class JobsSaidTransport(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(
        upload_to='jobs_said_transport/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Jobs said transport'
        verbose_name_plural = 'Jobs said transports'

    def __str__(self):
        return self.name


class KeyResponsibility(BaseModel):
    job = models.ForeignKey(JobsSaidTransport, on_delete=models.CASCADE, related_name='job_said_transport')
    text = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Key responsibility'
        verbose_name_plural = 'Key responsibility'

    def __str__(self):
        return self.text


class BenefitBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/benefit/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Benefit banner'
        verbose_name_plural = 'Benefit banners'

    def __str__(self):
        return self.banner_description


class HolidayObserver(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Holiday observer'
        verbose_name_plural = 'Holiday observers'

    def __str__(self):
        return self.description


class HolidayObserverItem(BaseModel):
    name = models.CharField(max_length=90)
    icon_image = models.FileField(
        upload_to='holiday/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Holiday observer item'
        verbose_name_plural = 'Holiday observer items'

    def __str__(self):
        return self.name


class AdditionalBenefits(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Additional benefits'
        verbose_name_plural = 'Additional benefits'

    def __str__(self):
        return self.description


class AdditionalBenefitsItem(BaseModel):
    name = models.CharField(max_length=90)
    icon_image = models.FileField(
        upload_to='additional_benefits/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Additional benefits item'
        verbose_name_plural = 'Additional benefits items'

    def __str__(self):
        return self.name


class CompanyCulture(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/company_culture/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='company_culture/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Company culture'
        verbose_name_plural = 'Company culture'

    def __str__(self):
        return self.banner_description


class CompanyCultureItem(BaseModel):
    title = models.CharField(max_length=90)
    definition = models.TextField()

    class Meta:
        verbose_name = 'Company culture item'
        verbose_name_plural = 'Company culture items'

    def __str__(self):
        return self.title


class LeasePurchaseBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/lease_purchase/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='lease_purchase/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Lease purchase banner'
        verbose_name_plural = 'Lease purchase banners'

    def __str__(self):
        return self.banner_description


class StandardLeaseDefinition(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Standard lease definition'
        verbose_name_plural = 'Standard lease definitions'

    def __str__(self):
        return self.description


class StandardLeaseCategory(BaseModel):
    title = models.CharField(max_length=90)

    class Meta:
        verbose_name = 'Standard lease category'
        verbose_name_plural = 'Standard lease categories'

    def __str__(self):
        return self.title


class StandardLeaseItem(BaseModel):
    category = models.ForeignKey(StandardLeaseCategory, on_delete=models.CASCADE)
    definition = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Standard lease item'
        verbose_name_plural = 'Standard lease items'

    def __str__(self):
        return self.category


class LeasePurchaseDefinition(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Lease purchase definition'
        verbose_name_plural = 'Lease purchase definitions'

    def __str__(self):
        return self.description


class LeasePurchaseCategory(BaseModel):
    title = models.CharField(max_length=90)

    class Meta:
        verbose_name = 'Lease purchase category'
        verbose_name_plural = 'Lease purchase categories'

    def __str__(self):
        return self.title


class LeasePurchaseItem(BaseModel):
    category = models.ForeignKey(LeasePurchaseCategory, on_delete=models.CASCADE)
    definition = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Lease purchase item'
        verbose_name_plural = 'Lease purchase items'

    def __str__(self):
        return self.category


class BenefitLeasingBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/benefits_leasing/', validators=[FileExtensionValidator(['jpg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='benefits_leasing/', validators=[FileExtensionValidator(['jpg'])]
    )

    class Meta:
        verbose_name = 'Benefit leasing banner'
        verbose_name_plural = 'Benefit leasing banners'

    def __str__(self):
        return self.banner_description


class BenefitLeasingInformation(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Benefit leasing information'
        verbose_name_plural = 'Benefit leasing informations'

    def __str__(self):
        return self.description


class BenefitLeasingInformationItem(BaseModel):
    definition = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Benefit leasing information item'
        verbose_name_plural = 'Benefit leasing information items'

    def __str__(self):
        return self.definition


class BenefitLeasingStar(BaseModel):
    definition = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Benefit leasing star'
        verbose_name_plural = 'Benefit leasing stars'

    def __str__(self):
        return self.definition


class AboutUs(BaseModel):
    telegram = models.CharField(max_length=40, blank=True, null=True)
    instagram = models.CharField(max_length=40, blank=True, null=True)
    facebook = models.CharField(max_length=40, blank=True, null=True)
    linkedin = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

    def __str__(self):
        return self.telegram


class Contact(BaseModel):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.full_name
