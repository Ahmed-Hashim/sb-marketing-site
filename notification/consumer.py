"""import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.template.loader import get_template

from notification.models import Notification


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.GROUP_NAME = 'user-notifications'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def published_post(self, event):
        data = json.loads(event["text"])

        id = data['id']
        thumbnail = data['thumbnail']
        message = data['message']
        category = data['category']
        scheduled_by = data['scheduled_by']
        published_date = data['published_date']
        fblink = data['fblink']
        # published_posts=Notification.objects.all().exclude(users=user)
        html = get_template("notification/noti.html").render(
            context={
                'id': id,
                'thumbnail': thumbnail,
                'message': message,
                'category': category,
                'scheduled_by': scheduled_by,
                'published_date': published_date,
                'fblink': fblink
            })
        self.send(text_data=html)

    def send_toast(self, event):
        data = (event["text"])
        self.send(text_data=data)
"""