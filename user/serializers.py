from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions, status
from rest_framework.validators import UniqueValidator

from user.models import Role


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError({'message': msg, 'status': status.HTTP_403_FORBIDDEN})
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=100)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        role = Role(user_id=user.id, is_admin=False)
        role.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
