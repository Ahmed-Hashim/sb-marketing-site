import logging
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404

from crm.models import Customer


def my_background_task():
    """customer_email = "ah.abolaban@gmail.com"
    user_email = 'info@soulnbody.net'
    email = EmailMultiAlternatives(
                    "subject",
                    "message",
                    user_email,
                    [customer_email],
                )


    email.send()"""
    print("IM WORKING ,,,,,,,")
