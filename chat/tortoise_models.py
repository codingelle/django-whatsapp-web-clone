
from tortoise import fields
from tortoise.models import Model

class ChatMessage(Model):
    """ use to store chat history message
        make used of tortoise ORM since its support asyncio ORM
    """ 
    id = fields.IntField(pk=True)
    room_id = fields.IntField(null=True)
    username = fields.CharField(max_length=50, null=True)
    message = fields.TextField()
    message_type = fields.CharField(max_length=50, null=True)
    image_caption = fields.CharField(max_length=50, null=True)
    date_created = fields.DatetimeField(null=True, auto_now_add=True)

    class Meta:
        table = 'chat_chatmessage'

    def __str__(self):
        return self.message
