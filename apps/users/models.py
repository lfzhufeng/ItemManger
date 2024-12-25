from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_LEVEL = (
        (0, 'normal'),
        (1, 'vip 1'),
        (2, 'vip 2'),
        (3, 'vip 3'),
        (4, 'vip 4'),
        (5, 'vip 5'),
        (6, 'vip 6'),
    )

    # 添加自定义字段
    id = models.AutoField(primary_key=True, verbose_name='用户ID')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=512, verbose_name='用户密码')
    email = models.EmailField(max_length=32, verbose_name='用户邮箱', null=True, blank=True)
    level = models.IntegerField(choices=USER_LEVEL, default=0, verbose_name='用户等级')

    # 内部Meta类，用于自定义表名
    class Meta:
        db_table = 'users'  # 设置自定义表名为 'custom_user'
        verbose_name = '用户'  # 管理界面显示的名称（单数）
        verbose_name_plural = '用户列表'  # 管理界面显示的名称（复数）

