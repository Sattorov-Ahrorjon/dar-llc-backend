from django.db import models
from tinymce.models import HTMLField
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import truncatechars
from django.utils import timezone

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

    @property
    def banner_text(self):
        return truncatechars(self.banner_description, 50)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Home banner'
        verbose_name_plural = 'Home banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)


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
        return truncatechars(self.description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.description, 50)


class CompanyCultureBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/culture/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    information_image = models.FileField(
        upload_to='about/culture/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    information_description = models.TextField()

    @property
    def short_description(self):
        return truncatechars(self.banner_description, 50)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Company culture banner'
        verbose_name_plural = 'Company culture banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)


class CompanyProgramsBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/programs/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_image = models.FileField(
        upload_to='about/programs/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Company programs banner'
        verbose_name_plural = 'Company programs banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class LeadershipTeamBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/teams/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Leadership team banner'
        verbose_name_plural = 'Leadership team banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_desc(self):
        return truncatechars(self.banner_description, 50)


class TeamMember(BaseModel):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='teams/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Team member'
        verbose_name_plural = 'Team members'

    def __str__(self):
        return self.full_name


class EquipmentBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/equipment/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    class Meta:
        verbose_name = 'Equipment banner'
        verbose_name_plural = 'Equipment banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class Equipment(BaseModel):
    title = models.CharField(max_length=150)
    model = models.CharField(max_length=250)
    engine = models.CharField(max_length=250)
    transmission = models.CharField(max_length=250)
    sleeper = models.CharField(max_length=250)
    inverter = models.CharField(max_length=250)
    apu = models.CharField(max_length=250)
    image = models.FileField(
        upload_to='equipment/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

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
        return truncatechars(self.banner_description, 60)

    @property
    def short_description(self):
        return truncatechars(self.banner_description, 60)


class MaintenanceBenefit(BaseModel):
    about = models.CharField(max_length=150)
    is_top = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Maintenance benefit text'
        verbose_name_plural = 'Maintenance benefits texts'

    def __str__(self):
        return self.about


class MaintenanceBenefitImage(BaseModel):
    image = models.FileField(
        upload_to='maintenance/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Maintenance benefit image'
        verbose_name_plural = 'Maintenance benefit images'

    def __str__(self):
        return f"Image num: {str(self.id)}"

    @property
    def item_link(self):
        return 'item_link'


class DarNewsBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/news/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Dar news banner'
        verbose_name_plural = 'Dar news banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class DarNews(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(
        upload_to='news/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Dar news'
        verbose_name_plural = 'Dar news'

    def __str__(self):
        return self.title

    @property
    def short_definition(self):
        return truncatechars(self.description, 50)


class ApartAdvantage(BaseModel):
    text = HTMLField()

    @property
    def short_text(self):
        return truncatechars(self.text, 100)

    class Meta:
        verbose_name = 'Apart advantage'
        verbose_name_plural = 'Apart advantage'

    def __str__(self):
        return truncatechars(self.text, 100)


class RefrigeratedDivisionBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/refrigerated/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='refrigerated/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Refrigerated division banner'
        verbose_name_plural = 'Refrigerated division banners'

    def __str__(self):
        return truncatechars(self.banner_description, 60)

    @property
    def short_description(self):
        return truncatechars(self.banner_description, 60)


class FlatbedDivisionBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/flatbed/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='flatbed/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Flatbed division banner'
        verbose_name_plural = 'Flatbed division banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class QualificationExpectationBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/qualification/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='qualification/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Qualification expectation banner'
        verbose_name_plural = 'Qualification expectation banners'

    def __str__(self):
        return truncatechars(self.banner_description, 60)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 60)


class QualificationExpectation(BaseModel):
    category = models.IntegerField(choices=QualificationCategory, default=1)
    instance = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Qualification expectation'
        verbose_name_plural = 'Qualification expectations'

    def __str__(self):
        return truncatechars(self.instance, 60)

    @property
    def short_descr(self):
        return truncatechars(self.instance, 60)


class QualificationExpectationImage(BaseModel):
    category = models.IntegerField(choices=QualificationCategory, default=1)
    image = models.FileField(upload_to='qualification_expectation/',
                             validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    class Meta:
        verbose_name = 'Qualification expectation image'
        verbose_name_plural = 'Qualification expectation images'

    def __str__(self):
        return f"{dict(QualificationCategory).get(self.category)} {self.id}"


class PayBenefitBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/pay_benefit/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='pay_benefit/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Pay benefit banner'
        verbose_name_plural = 'Pay benefits banner'

    def __str__(self):
        return truncatechars(self.banner_description, 60)

    @property
    def short_desc(self):
        return truncatechars(self.banner_description, 60)


class PayBenefitItem(BaseModel):
    category = models.IntegerField(choices=AboutPayBenefitCategory, default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='about_pay_benefit/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Pay Benefit Item'
        verbose_name_plural = 'Pay Benefit Items'

    def __str__(self):
        return self.title


class PayBenefitTable(BaseModel):
    position_type = models.CharField(max_length=120, blank=True, null=True)
    dry_van = models.CharField(max_length=120, blank=True, null=True)
    refrigerated = models.CharField(max_length=120, blank=True, null=True)
    flatbed = models.CharField(max_length=120, blank=True, null=True)
    team_bonus = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Pay Benefit Table'
        verbose_name_plural = 'Pay Benefit Tables'

    def __str__(self):
        return f"{self.id} {self.position_type}"


class DriverTrainingProgramBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/training_program/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Driver training program banner'
        verbose_name_plural = 'Driver training program banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


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
        upload_to='banner/cdl_holders/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'CDL holder banner'
        verbose_name_plural = 'CDL holder banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class CDLHolderAdvantage(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_image = models.FileField(
        upload_to='cdl_holders/advantage/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'CDL holder advantage'
        verbose_name_plural = 'CDL holder advantage'

    def __str__(self):
        return self.title

    @property
    def short_definition(self):
        return truncatechars(self.description, 50)


class DriverAwardBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/driver_award/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='driver_award/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    @property
    def banner_text(self):
        return truncatechars(self.banner_description, 50)

    class Meta:
        verbose_name = 'Driver award banner'
        verbose_name_plural = 'Driver award banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)


class TransportLeadershipElite(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Transport leadership elite'
        verbose_name_plural = 'Transport leadership elites'

    def __str__(self):
        return truncatechars(self.description, 80)

    @property
    def short_definition(self):
        return truncatechars(self.description, 80)


class SafetyChampionAwards(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Safety champion awards'
        verbose_name_plural = 'Safety champion awards'

    def __str__(self):
        return truncatechars(self.description, 60)

    @property
    def short_desc(self):
        return truncatechars(self.description, 60)


class JobsSaidTransportBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/jobs_said_transport/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    @property
    def banner_text(self):
        return truncatechars(self.banner_description, 50)

    class Meta:
        verbose_name = 'Jobs said transport banner'
        verbose_name_plural = 'Jobs said transport banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)


class JobsSaidTransportCategory(BaseModel):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Jobs said transport category'
        verbose_name_plural = "Jobs said transport categories"

    def __str__(self):
        return self.title


class JobsSaidTransportLocation(BaseModel):
    location = models.CharField(max_length=180)

    class Meta:
        verbose_name = 'Jobs said transport location'
        verbose_name_plural = 'Jobs said transport locations'

    def __str__(self):
        return truncatechars(self.location, 60)

    @property
    def location_link(self):
        return truncatechars(self.location, 60)


class JobsSaidTransport(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(
        upload_to='jobs_said_transport/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    published_date = models.DateField(blank=True, null=True, default=timezone.now)
    category = models.ForeignKey(to='api.JobsSaidTransportCategory', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(to='api.JobsSaidTransportLocation', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Jobs said transport'
        verbose_name_plural = 'Jobs said transports'

    def __str__(self):
        return self.name

    @property
    def short_desc(self):
        return truncatechars(self.description, 50)


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
        upload_to='banner/benefit/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()

    class Meta:
        verbose_name = 'Benefit banner'
        verbose_name_plural = 'Benefit banners'

    def __str__(self):
        return truncatechars(self.banner_description, 60)

    @property
    def short_definition(self):
        return truncatechars(self.information_description, 60)


class HolidayObserver(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Holiday observer'
        verbose_name_plural = 'Holiday observers'

    def __str__(self):
        return truncatechars(self.description, 50)

    @property
    def banner_text(self):
        return truncatechars(self.description, 50)


class AdditionalBenefits(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Additional benefits'
        verbose_name_plural = 'Additional benefits'

    def __str__(self):
        return truncatechars(self.description, 70)

    @property
    def short_description(self):
        return truncatechars(self.description, 70)


class CompanyCulture(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/company_culture/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='company_culture/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Company culture'
        verbose_name_plural = 'Company culture'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.banner_description, 50)


class CompanyCultureItem(BaseModel):
    title = models.CharField(max_length=90)
    definition = models.TextField()

    class Meta:
        verbose_name = 'Company culture item'
        verbose_name_plural = 'Company culture items'

    def __str__(self):
        return self.title

    @property
    def short_definition(self):
        return truncatechars(self.definition, 50)


class LeasePurchaseBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/lease_purchase/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='lease_purchase/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Lease purchase banner'
        verbose_name_plural = 'Lease purchase banners'

    def __str__(self):
        return truncatechars(self.banner_description, 50)

    @property
    def short_desc(self):
        return truncatechars(self.banner_description, 50)


class StandardLeaseDefinition(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Standard lease definition'
        verbose_name_plural = 'Standard lease definitions'

    def __str__(self):
        return truncatechars(self.description, 60)

    @property
    def short_definition(self):
        return truncatechars(self.description, 60)


class StandardLeaseItem(BaseModel):
    title = models.CharField(max_length=90)
    description = HTMLField()

    class Meta:
        verbose_name = 'Standard lease item'
        verbose_name_plural = 'Standard lease items'

    def __str__(self):
        return self.title

    @property
    def short_desc(self):
        return truncatechars(self.description, 60)


class LeasePurchaseDefinition(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Lease purchase definition'
        verbose_name_plural = 'Lease purchase definitions'

    def __str__(self):
        return truncatechars(self.description, 50)

    @property
    def short_desc(self):
        return truncatechars(self.description, 50)


class LeasePurchaseItem(BaseModel):
    title = models.CharField(max_length=90)
    description = HTMLField()

    class Meta:
        verbose_name = 'Lease purchase item'
        verbose_name_plural = 'Lease purchase items'

    def __str__(self):
        return self.title

    @property
    def short_desc(self):
        return truncatechars(self.description, 50)


class LeasePurchaseImage(BaseModel):
    image = models.FileField(upload_to='lease_purchase/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    class Meta:
        verbose_name = 'Lease purchase image'
        verbose_name_plural = 'Lease purchase images'

    def __str__(self):
        return f"Image ID: {self.id}"

    @property
    def obj_link(self):
        return f'{self.id} image_link'


class BenefitLeasingBanner(BaseModel):
    banner_description = models.TextField()
    banner_image = models.FileField(
        upload_to='banner/benefits_leasing/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    information_description = models.TextField()
    information_image = models.FileField(
        upload_to='benefits_leasing/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    class Meta:
        verbose_name = 'Benefit leasing banner'
        verbose_name_plural = 'Benefit leasing banners'

    def __str__(self):
        return truncatechars(self.banner_description, 70)

    @property
    def banner_desc(self):
        return truncatechars(self.banner_description, 70)


class BenefitLeasingInformation(BaseModel):
    description = models.TextField()

    class Meta:
        verbose_name = 'Benefit leasing information'
        verbose_name_plural = 'Benefit leasing informations'

    def __str__(self):
        return truncatechars(self.description, 50)

    @property
    def short_definition(self):
        return truncatechars(self.description, 50)


class BenefitLeasingInformationItem(BaseModel):
    definition = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Benefit leasing information item'
        verbose_name_plural = 'Benefit leasing information items'

    def __str__(self):
        return truncatechars(self.definition, 70)

    @property
    def short_definition(self):
        return truncatechars(self.definition, 50)


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
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.full_name


class QuickLink(BaseModel):
    submit_pics = models.CharField(max_length=180)
    driver_verification = models.CharField(max_length=180)

    class Meta:
        verbose_name = 'Quick link'
        verbose_name_plural = 'Quick links'

    def __str__(self):
        return f"{self.id} Quick link"
