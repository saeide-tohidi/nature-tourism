from rest_framework import serializers
from users.models import UserProfile, CustomUser
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='تکرار گذرواژه')
    phoneNo = serializers.CharField(required=True, label='موبایل')

    class Meta:
        model = CustomUser
        fields = ['phoneNo', 'password', 're_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
