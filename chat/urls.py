
from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('history/<str:room_id>/', views.history, name='history'),
    path('<str:group_id>/', views.room, name='room'),
]
