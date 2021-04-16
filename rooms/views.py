from rooms.models import Room
from rooms.serializer import RoomSerializer
from rest_framework.generics import ListAPIView


class ListRoomsView(ListAPIView):
        queryset = Room.objects.all()
        serializer_class = RoomSerializer

