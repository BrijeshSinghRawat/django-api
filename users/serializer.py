from rest_framework import serializers
from .models import User

class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id","username","first_name","last_name","email","avatar","superhost")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","first_name","last_name","email","avatar","superhost","favs")

class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
