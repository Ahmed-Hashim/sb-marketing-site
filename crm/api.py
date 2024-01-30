from ninja import NinjaAPI
from .models import RequestClinicSystemPackage, RequestHospitalSystemPackage
from .schemas import (
    ClinicIn,
    HosbitalIn,
    RequestClinicSystemPackageSchema,
    RequestHospitalSystemPackageSchema,
)

app = NinjaAPI()


@app.post("/addclinicr/")
def create_request_c(request, payload: ClinicIn):
    clinicr = RequestClinicSystemPackage.objects.create(**payload.dict())
    return {"id": clinicr.id}


@app.post("/addhosbitalr/")
def create_request_h(request, payload: HosbitalIn):
    hosbitalr = RequestHospitalSystemPackage.objects.create(**payload.dict())
    return {"id": hosbitalr.id}
