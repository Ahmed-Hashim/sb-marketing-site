from django.urls import path,include
from .views import *


urlpatterns = [
                path("notification",notification_list,name='notification') ,
                path("remove_notification/<int:id>",remove_notification,name='remove_notification') 

]