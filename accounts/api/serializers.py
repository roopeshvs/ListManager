from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

from rest_framework import serializers

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'dob', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}, 'dob': {'write_only': True}, 'first_name': {'write_only': True}, 'last_name': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            dob = validated_data['dob'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(user.password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
