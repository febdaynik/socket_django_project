import json, random, time

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from integers.models import Message, Room


class ClickerConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_group_name = str(self.scope['url_route']['kwargs']['room_game'])
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)
		await self.accept()
		# await self.online(type='connect', value=1, rid=self.room_group_name)
 
	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)
		# await self.online(type='disconnect', value=-1, rid=self.room_group_name)


	@database_sync_to_async
	def online(self, type, value, rid):
		print(type, value, rid)
		# if type == 'connect':
		# try:
		# 	nedo_bd[rid] = value
		# except KeyError:
		# 	nedo_bd[rid] += value 
		# elif type == 'disconnect':
		# nedo_bd[rid] += value

		# print(nedo_bd)
		# Message.objects.create(text=message)

	@database_sync_to_async
	def new_message(self, rid, score):
		upd = Room.objects.filter(room_id=str(rid)).update(score=int(score))
		if upd == 0:
			Room.objects.create(room_id=rid, score=score)



	# Принимаем сообщение от пользователя
	async def receive(self, text_data=None, bytes_data=None):
		text_data_json = json.loads(text_data)
		score = text_data_json['score']
		room_id = text_data_json['room_id']

		await self.new_message(rid=room_id, score=score)
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'send_mess',
				'score': score,
			}
		)

	# Метод для отправки сообщения клиентам
	async def send_mess(self, event):
		# Получаем сообщение от receive
		score = event['score']
		# Отправляем сообщение клиентам
		await self.send(text_data=json.dumps({
			'score': score,
		}, ensure_ascii=False))
	