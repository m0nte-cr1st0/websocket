from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from .models import Chat


def index(request):
    return render(request, 'chat/index.html', {})

print(User.objects.all())
# print(Chat.objects.first().users.all())
class RoomDetail(DetailView):
    def get(self, *args, **kwargs):
        user = User.objects.get(username=kwargs['room_name'])
        chat = Chat.objects.filter(users__in=[user.id, self.request.user.id]).first()
        if not chat:
            chat = Chat.objects.create()
            chat.users.add(self.request.user.id)
            chat.users.add(user.id)
        return render(self.request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(kwargs['room_name'])),
            'chat': chat
        })


class ChatListView(ListView):
    model = User
    template_name = 'chat/messages_list.html'

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.pk)
