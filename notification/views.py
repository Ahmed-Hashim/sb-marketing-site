from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Notification


def notification_list(request):
    user=get_object_or_404(User,id=request.user.id)
    notifications=Notification.objects.all().exclude(users=user)
    return render (request,'notification/notify_list.html',{'notifications':notifications})



def remove_notification(request,id):
    notification=get_object_or_404(Notification,id=id)
    user=request.user.id
    notification.users.add(user)
    notification.save()
    return redirect(notification_list)
