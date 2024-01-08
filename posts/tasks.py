from __future__ import absolute_import, unicode_literals
from django.contrib.auth.models import User
from celery import shared_task, Celery
from django_celery_beat.models import PeriodicTask, PeriodicTasks, ClockedSchedule
import pytz
from .models import AlmazadiProducts, Category, Post, Schedule, PublishedPost
from datetime import datetime
from .uploadtofacebook import *
from pytz import timezone as tz
from .uploadimg import uploadimg
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail
from .get_posts import main, products_checking

app = Celery()


@shared_task
def Schedule_Posts(user_id, postid):
    user = User.objects.get(id=user_id)
    time = datetime.now() + timedelta(minutes=1)
    user_timezone = pytz.timezone(user.profile.timezone)
    london_dt = user_timezone.localize(time)
    give_this_to_celery = london_dt.astimezone(pytz.UTC)
    print(user.profile.timezone)
    clocked_schedule, created = ClockedSchedule.objects.get_or_create(
        clocked_time=give_this_to_celery.strftime('%Y-%m-%d %H:%M:%S'),
    )
    PeriodicTask.objects.create(
        name=f'Schedule Post-{give_this_to_celery.strftime("%Y-%m-%d %H:%M:%S")}',
        task='post.tasks.checking_celery',
        start_time=give_this_to_celery.strftime('%Y-%m-%d %H:%M:%S'),
        clocked=clocked_schedule,
        # args=[str(postid)],
        enabled=True,
        one_off=True
    )
    PeriodicTasks.update_changed()
    return print(f"Post has been scheduled it will publish on {london_dt}")


@shared_task  # for testing only
def Publish_Post():
    print("Publishing post")
    x = "Publishing post"
    return x


@shared_task
def checking_celery(email):
    subject = 'Hey from celery'
    message = f'H Admin, Celery is working.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)


@shared_task(soft_time_limit=30, time_limit=90)
def refresh_products():
    count = 0
    links = products_checking()
    for link in links:
        try:
            message = f"{link['add_title']} \n متوفر الان على تطبيق المزادي\n من خلال {link['add_owner']}"
            if link['category'] == 'Multimédia':
                categorys = "Multimedia"
            elif link['category'] == 'Productive Family':
                categorys = 'Productive Fami'
            elif link['category'] == 'Professional Equipment':
                categorys = 'Professional Eq'
            else:
                categorys = link['category']
                category = Category.objects.get(name__contains=categorys)
            if "store" in link['link']:
                edit_link = f"https://almazadi.com/admin/products/{link['link'].split('/')[-1]}/edit"
            else:
                edit_link = f"https://almazadi.com/admin/posts/{link['link'].split('/')[-1]}/edit"
            if link['add_image'] != "https://almazadi.com/storage/app/default/picture.jpg":
                AlmazadiProducts.objects.create(
                    add_title=link['add_title'],
                    imagelink=link['add_image'],
                    edit_link=edit_link,
                    add_link=link['link'],
                    owner=link['add_owner'],
                    category=category,
                    message=message
                )
                count += 1
                print(f"new ad/s added .")
            else:
                print('no picture')
        except Exception as e:
            print(e)
    if count > 0:
        print(f"{count} new ad/s added .")
        return app.control.purge()
    else:
        print(f"0 New ads.")
        return app.control.purge()
