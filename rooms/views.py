from rooms.models import Room
from rooms.serializer import RoomSerializer, WriteRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RoomsView(APIView):

        def get(self, request):
                room = Room.objects.all()
                serializer = RoomSerializer(room,many=True).data
                return Response(status=status.HTTP_200_OK,data=serializer)

        def post(self, request):
                if not request.user.is_authenticated:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                room_serializer = WriteRoomSerializer(data=request.data)
                if room_serializer.is_valid():
                        room = room_serializer.save(user=request.user)
                        serializer = RoomSerializer(room)
                        return Response(status=status.HTTP_200_OK,data=serializer.data)
                else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)




class RoomView(APIView):
        def get_room_object(self, pk):
                try:
                        room = Room.objects.get(pk=pk)
                        return room
                except Room.DoesNotExist:
                        return None
        def get(self, request, pk):
                room = self.get_room_object(pk)
                if room is not None:
                        serializer = RoomSerializer(room)
                        return Response(status=status.HTTP_200_OK, data=serializer.data)
                else:
                        return Response(status=status.HTTP_404_NOT_FOUND)
        def put(self, request, pk):
                room = self.get_room_object(pk)
                if room is not None:
                        if room.user != request.user:
                                return Response(status=status.HTTP_403_FORBIDDEN)
                        serializer = WriteRoomSerializer(room,data=request.data,partial=True)
                        if serializer.is_valid():
                                return Response(serializer.save())
                        else:
                                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
                else:
                        return Response(status=status.HTTP_404_NOT_FOUND)

        def delete(self, request, pk):
                room = self.get_room_object(pk)
                if room is not None:
                        if room.user != request.user:
                                return Response(status=status.HTTP_403_FORBIDDEN)
                        room.delete()
                        return Response(status=status.HTTP_200_OK)
                else:
                        return Response(status=status.HTTP_404_NOT_FOUND)


