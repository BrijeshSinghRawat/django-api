from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer,WriteUserSerializer
from rest_framework.permissions import IsAuthenticated

class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response(UserSerializer(request.user).data)

    def put(self,request):
        serializer= WriteUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

class UserView(APIView):
    def get(self,request, pk):
        pass
    def post(self,request, pk):
        pass
