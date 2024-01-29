from django.contrib import admin
from django.utils.html import format_html
from .models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["Situation", "industry"]
    list_display = [
        "clinic_or_hosbital_name",
        "first_name",
        "last_name",
        "lead_referral_source",
        "industry",
        "address",
        "land_phone_number",
        "phone_number",
        "email",
        "website",
        "status",
        "last_contact_date",
        "_",
    ]
    search_fields = [
        "clinic_or_hosbital_name",
        "first_name",
        "last_name",
        "lead_referral_source",
        "industry",
        "land_phone_number",
        "phone_number",
        "email",
        "website",
        "Situation",
    ]
    list_per_page = 25

    def _(self, obj):
        if obj.Situation == "Active":
            return True
        elif obj.Situation == "Prospect":
            return None
        elif obj.Situation == "Email Sent":
            return True
        else:
            return False

    _.boolean = True

    def status(self, obj):
        if obj.Situation == "Active":
            color = "#28a745"
        elif obj.Situation == "Prospect":
            color = "#fea95e"
        elif obj.Situation == "Email Sent":
            color = "SlateBlue"
        else:
            color = "red"
        return format_html(
            '<strong><p style="color:{}">{}</p></strong>'.format(color, obj.Situation)
        )

    status.allow_tags = True


admin.site.register(Note)
admin.site.register(Customer_Email)
admin.site.register(Contact)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Industry)
admin.site.register(Whatsapp_Template)
admin.site.register(Whatsapp_Messages)


class RequestClinicSystemPackageAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone_number",
        "email",
        "clinic_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]
    list_filter = [
        "name",
        "phone_number",
        "email",
        "clinic_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]


admin.site.register(RequestClinicSystemPackage, RequestClinicSystemPackageAdmin)


class RequestHospitalSystemPackageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "name",
        "hosbital",
        "phone_number",
        "email",
        "hospital_beds_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]
    list_display = [
        "title",
        "name",
        "hosbital",
        "phone_number",
        "email",
        "hospital_beds_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]


admin.site.register(RequestHospitalSystemPackage, RequestHospitalSystemPackageAdmin)
