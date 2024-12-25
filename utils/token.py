from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import CustomUser

class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = CustomUser.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)

            return {
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
        raise serializers.ValidationError("Invalid credentials")
