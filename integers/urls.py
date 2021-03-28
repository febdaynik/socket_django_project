from django.urls import path
from . import views

urlpatterns = [
	# path('', chat),
	# path('clicker/', views.game),
	path('clicker/<int:room_game>', views.game),
	path('chat/', views.chat),
]