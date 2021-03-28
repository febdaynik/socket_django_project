from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	text = models.CharField(max_length=255)


class Room(models.Model):
	# username = models.ForeignKey(User, on_delete=models.CASCADE, default=True, related_name="username_room", null=True)
	room_id = models.CharField(max_length=255)
	score = models.IntegerField()