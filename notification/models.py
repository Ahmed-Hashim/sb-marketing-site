from django.db import models
from django.db.models.signals import post_save
from posts.models import PublishedPost
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    post=models.ForeignKey(PublishedPost,on_delete=models.CASCADE)
    users=models.ManyToManyField(User,related_name='notifications',blank=True)

def create_notification(sender,**kwargs):
    if kwargs['created']:
        Notification.objects.create(post=kwargs['instance'])
post_save.connect(create_notification,sender=PublishedPost)