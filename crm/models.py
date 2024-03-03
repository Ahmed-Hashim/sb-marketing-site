from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from .fields import NonStrippingTextField
from members.models import Profile
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

TITLE = (
    ("MR", "MR"),
    ("MRS", "MRS"),
    ("DR", "DR"),
)


# Create your models here.
class Customer(models.Model):
    STATUS = (
        ("Prospect", "Prospect"),
        ("Email Sent", "Email Sent"),
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Suspended", "Suspended"),
    )
    title = models.CharField(max_length=25, choices=TITLE, null=True, blank=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    lead_referral_source = models.CharField(max_length=120, blank=True, null=True)
    industry = models.CharField(max_length=120, default="غير معلوم")
    clinic_or_hosbital_name = models.CharField(max_length=120, blank=False, null=False)
    address = models.CharField(max_length=190, null=True, blank=True)
    street = models.CharField(max_length=190, null=True, blank=True)
    land_phone_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=190, null=True, blank=True)
    date_to_meeting = models.DateField(null=True, blank=True)
    time_date_to_meeting = models.TimeField(null=True, blank=True)
    assigend_to = models.ForeignKey(
        Profile, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    Situation = models.CharField(
        null=True, blank=True, choices=STATUS, default="Prospect", max_length=100
    )
    background_info = models.TextField(max_length=500, null=True, blank=True)
    last_contact_date = models.CharField(null=True, blank=True, max_length=25)
    facebook_url = models.CharField(max_length=150, null=True, blank=True)
    instagram_url = models.CharField(max_length=150, null=True, blank=True)
    twitter_url = models.CharField(max_length=150, null=True, blank=True)
    linkedin_url = models.CharField(max_length=150, null=True, blank=True)
    skype_url = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(("slug"), blank=True, null=True)

    def __str__(self):
        return self.clinic_or_hosbital_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.clinic_or_hosbital_name)
        super(Customer, self).save(*args, **kwargs)


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=50)

    def __str__(self):
        return str(self.company)


class Industry(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.type)


class Note(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]


class Customer_Email(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    file_upload = models.FileField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.company, self.subject)


class Whatsapp_Template(models.Model):
    TYPES = {("TEXT", "TEXT"), ("IMAGE", "IMAGE"), ("PDF", "PDF"), ("VIDEO", "VIDEO")}
    LANG = (
        ("AR", "AR"),
        ("EN", "EN"),
        ("FR", "FR"),
    )
    title = models.CharField(max_length=25)
    type = models.CharField(choices=TYPES, default="TEXT", max_length=10)
    message = NonStrippingTextField(max_length=1000)
    file_upload = models.FileField(
        null=True, blank=True, upload_to="whatsapp_templates/"
    )
    language = models.CharField(choices=LANG, max_length=2, null=True, blank=True)
    template_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)


class Whatsapp_Messages(models.Model):
    TYPES = {("TEXT", "TEXT"), ("IMAGE", "IMAGE"), ("PDF", "PDF"), ("VIDEO", "VIDEO")}
    company = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="whatappmsg"
    )
    type = models.CharField(choices=TYPES, default="TEXT", max_length=10)
    message = models.TextField(max_length=1000)
    file_upload = models.FileField(
        null=True, blank=True, upload_to="whatsapp_templates/"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}-{self.company}"


class RequestClinicSystemPackage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    clinic_count = models.PositiveIntegerField()
    departement_count = models.PositiveIntegerField()
    doctors_count = models.PositiveIntegerField()
    users_count = models.PositiveIntegerField()
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.name, self.phone_number, self.clinic_count, self.date
        )


class RequestHospitalSystemPackage(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    hosbital = models.CharField(max_length=120, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    hospital_beds_count = models.PositiveIntegerField(blank=False, null=False)
    departement_count = models.PositiveIntegerField(blank=False, null=False)
    doctors_count = models.PositiveIntegerField(blank=False, null=False)
    users_count = models.PositiveIntegerField(blank=False, null=False)
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
