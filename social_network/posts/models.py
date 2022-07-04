from django.db import models
import uuid

class Wall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique wall object ID')
    book = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.TextField('Name', max_length=255, help_text='Name of the wall')
    pin_to_top = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


