from django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "lead_referral_source",
            "industry",
            "clinic_or_hosbital_name",
            "address",
            "street",
            "email",
            "website",
            "Situation",
            "background_info",
            "facebook_url",
            "instagram_url",
            "twitter_url",
            "linkedin_url",
            "skype_url",
            "land_phone_number",
            "phone_number",
        )
        labels = {
            "clinic_or_hosbital_name": "Clinic / Hosbital",
        }

        widgets = {
            "title": forms.Select(attrs={"class": "form-control", "id": "title"}),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "firstname"}
            ),
            "middle_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "lead_referral_source": forms.TextInput(attrs={"class": "form-control"}),
            "industry": forms.TextInput(attrs={"class": "form-control"}),
            "clinic_or_hosbital_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "Situation": forms.Select(attrs={"class": "form-control"}),
            "background_info": forms.Textarea(attrs={"class": "form-control"}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
            "linkedin_url": forms.TextInput(attrs={"class": "form-control"}),
            "skype_url": forms.TextInput(attrs={"class": "form-control"}),
            "land_phone_number": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
        }


class Customer_Email_Form(forms.ModelForm):
    class Meta:
        model = Customer_Email
        fields = ["subject", "file_upload", "message", "sender", "company"]
        subject = forms.CharField(label="Subject")
        file_upload = forms.FileField(label="attatchments")
        message = forms.CharField(label="Message")
        sender = forms.CharField(label="Sender")
        company = forms.CharField(label="Company")
        widgets = {
            "file_upload": forms.FileInput(attrs={"class": "filefield"}),
            "sender": forms.TextInput(
                attrs={"class": "form-control", "id": "sender", "type": "hidden"}
            ),
            "company": forms.TextInput(
                attrs={"class": "form-control", "id": "company", "type": "hidden"}
            ),
        }


class Addcontanct(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        full_name = forms.CharField(label="Full Name")
        position = forms.CharField(label="Position")
        phone_number = forms.CharField(label="Phone Number")
        company = forms.CharField(label="Message")
        widgets = {
            "company": forms.TextInput(
                attrs={
                    "type": "hidden",
                    "id": "company",
                }
            )
        }


class Addnote(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        writer = forms.CharField()
        company = forms.CharField()
        notes = forms.CharField(label="Note")
        widgets = {
            "company": forms.TextInput(
                attrs={
                    "id": "company",
                    "type": "hidden",
                }
            ),
            "writer": forms.TextInput(
                attrs={
                    "id": "user",
                    "type": "hidden",
                }
            ),
        }


class AddTemplate(forms.ModelForm):
    class Meta:
        model = Whatsapp_Template
        fields = "__all__"
        tilte = forms.CharField()
        type = forms.CharField()
        message = forms.CharField()
        template_by = forms.CharField()
        file_upload = forms.FileField()
        widgets = {
            "tilte": forms.TextInput(
                attrs={
                    "id": "title-temp",
                }
            ),
            "type": forms.Select(
                attrs={
                    "id": "type-temp",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "id": "message-temp",
                }
            ),
            "template_by": forms.TextInput(
                attrs={
                    "id": "template-by",
                    "type": "hidden",
                }
            ),
            "file_upload": forms.FileInput(
                attrs={
                    "id": "file-temp",
                }
            ),
        }


class PhoneSelectForm(forms.Form):
    def __init__(self, company_id, *args, **kwargs):
        super(PhoneSelectForm, self).__init__(*args, **kwargs)

        # Define a choices list to store phone numbers
        phone_choices = []

        # Fetch phone numbers from Customer model for the specified company
        customer = Customer.objects.get(id=company_id)
        if customer.land_phone_number:
            phone_choices.append(
                (
                    customer.land_phone_number,
                    f"Land Phone - {customer.clinic_or_hosbital_name} - {customer.land_phone_number}",
                )
            )
        if customer.phone_number:
            phone_choices.append(
                (
                    customer.phone_number,
                    f"Mobile Phone - {customer.clinic_or_hosbital_name} - {customer.phone_number}",
                )
            )

        # Fetch phone numbers from Contact model for the specified company
        contacts = Contact.objects.filter(company=customer)
        for contact in contacts:
            phone_choices.append(
                (
                    contact.phone_number,
                    f"{contact.position} - {contact.full_name} ({customer.clinic_or_hosbital_name}) - {contact.phone_number}",
                )
            )

        # Define the phone number field with the collected choices
        self.fields["phone_number"] = forms.ChoiceField(
            choices=phone_choices, widget=forms.Select(attrs={"class": "form-control"})
        )
