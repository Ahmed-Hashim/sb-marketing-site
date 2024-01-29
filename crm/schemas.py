from ninja import ModelSchema
from .models import RequestClinicSystemPackage, RequestHospitalSystemPackage
from ninja import Schema


class RequestClinicSystemPackageSchema(ModelSchema):
    class Meta:
        model = RequestClinicSystemPackage
        fields = "__all__"


class RequestHospitalSystemPackageSchema(ModelSchema):
    class Meta:
        model = RequestHospitalSystemPackage
        fields = "__all__"


class ClinicIn(Schema):
    name: str
    phone_number: str
    email: str
    clinic_count: int
    departement_count: int
    doctors_count: int
    users_count: int
    details: str


class HosbitalIn(Schema):
    name: str
    title: str
    hosbital: str
    phone_number: str
    email: str
    hospital_beds_count: int
    departement_count: int
    doctors_count: int
    users_count: int
    details: str
