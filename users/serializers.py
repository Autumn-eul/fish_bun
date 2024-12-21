from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        if not validated_data.get("email").endswith("@gmail.com"):
            raise serializers.ValidationError("너 gmail 아니잖아!")
        
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "address", "contact", "gender")
