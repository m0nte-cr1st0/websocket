from django.urls import path

from .views import index, RoomDetail, ChatListView

urlpatterns = [
    path('', index, name='index'),
    path('messages/', ChatListView.as_view(), name='messages'),
    path('<str:room_name>/', RoomDetail.as_view(), name='room'),
]
