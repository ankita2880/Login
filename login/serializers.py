from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
    

class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    mobile_no = serializers.CharField(max_length=30)
    token = serializers.CharField(required=False, read_only=True)


    def validate(self, data):
        print('dataaaaaaaaaaaaaaaaaa',data)
        if User.objects.filter(username=data).exists():
            raise serializers.ValidationError("Username already exists.")
        # return data
        # user,email,password validator
        # user_id = data.get("user_id", None)
        # password = data.get("password", None)
        # if not user_id and not password:
        #     raise ValidationError("Details not entered.")
        # user = None
        # # if the email has been passed
        # if '@' in user_id:
        #     user = User.objects.filter(
        #         Q(email=user_id) &
        #         Q(password=password)
        #         ).distinct()
        #     if not user.exists():
        #         raise ValidationError("User credentials are not correct.")
        #     user = User.objects.get(email=user_id)
        # else:
        #     user = User.objects.filter(
        #         Q(username=user_id) &
        #         Q(password=password)
        #     ).distinct()
        #     if not user.exists():
        #         raise ValidationError("User credentials are not correct.")
        #     user = User.objects.get(username=user_id)
        # if user.ifLogged:
        #     raise ValidationError("User already logged in.")
        # user.ifLogged = True
        # data['token'] = uuid4()
        # user.token = data['token']
        # user.save()
        # return data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        mobile_no = data.get('mobile_no')

        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            mobile_no=mobile_no,
        )
        return data


    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'mobile_no',
            'token',
        )

        read_only_fields = (
            'token',
        )
    