import json
from channels.generic.websocket import AsyncWebsocketConsumer
#from asgiref.sync import await_to_sync
from chat.services import chat_save_message



class ChatConsumer(AsyncWebsocketConsumer):
    """ handshake websocket front end """

    room_name = None
    room_group_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, code):
        # Leave room group
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        image_caption = text_data_json['image_caption']
        message_type = text_data_json['message_type']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': self.scope['user'].username.title(),
                'message': message,
                'message_type': message_type,
                'image_caption': image_caption
            }
        )

        await chat_save_message(
            username=self.scope['user'].username.title(),
            room_id=self.room_name,
            message=message,
            message_type=message_type,
            image_caption=image_caption
        )


    # Receive message from room group
    async def chat_message(self, event):
        """ exhange message here """
        message = event['message']
        username = event['username']
        image_caption = event['image_caption']
        message_type = event['message_type']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'image_caption': image_caption,
            'message_type': message_type
        }))
