from django.shortcuts import render, redirect
from .models import Message, Room
import random

def index(request):
	return render(request, 'index.html', context={'text':'Hey'})

def chat(request):
	msg = Message.objects.all()
	return render(request, 'room.html', {'msgs': msg})

def game(request, room_game):
	score_room = Room.objects.filter(room_id=str(room_game))
	# if len(score_room) == 0:
		# score_room = {'room_id': str(room_game), 'score': 0}
	print(score_room)
	if 1 <= room_game <= 3:
		return render(request, 'clicker.html', {'url': room_game, 'score_room': score_room})

	return redirect(f'/clicker/{random.randint(1,3)}')
	# return render(request, 'clicker.html', {'url': room_game})