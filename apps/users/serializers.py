from rest_framework import serializers
from .models import CustomUser
from django.conf import settings
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'confirm_password','image', 'role', 'name']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'status','image','image_url', 'name']

    def get_image_url(self, obj):
        """
        Method to return the full URL of the image field.
        """
        if obj.image:
            return settings.BASE_URL + obj.image.url
        return None


class UpdateStatusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['status']