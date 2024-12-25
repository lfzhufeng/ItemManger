from rest_framework import serializers
from apps.users.models import CustomUser  # 假设你使用的是自定义用户模型

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # 密码设置为只写
    confirm_password = serializers.CharField(write_only=True, required=True)  # 确认密码字段

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'date_joined', 'is_active']
        read_only_fields = ['id', 'date_joined', 'is_active']  # 这些字段不允许通过API修改

    def validate(self, data):
        # 验证密码与确认密码是否一致
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        # 移除确认密码字段
        validated_data.pop('confirm_password')
        # 创建用户并加密密码
        user = CustomUser.objects.create_user(**validated_data)
        password = validated_data.pop
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # 更新用户信息
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)

        # 更新用户非密码字段
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # 如果提供了密码，则更新密码
        if password:
            instance.set_password(password)

        instance.save()
        return instance
