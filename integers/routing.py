from django.urls import path

from integers.consumers.chat_consumers import ChatConsumer
from integers.consumers.clicker_consumers import ClickerConsumer


ws_urlpatterns = [
	path('ws/chat/', ChatConsumer.as_asgi()),
	path('ws/clicker/<int:room_game>', ClickerConsumer.as_asgi()),
]