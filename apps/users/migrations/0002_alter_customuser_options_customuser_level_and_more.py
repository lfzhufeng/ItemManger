# Generated by Django 5.1.4 on 2024-12-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户列表'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(choices=[(0, 'normal'), (1, 'vip 1'), (2, 'vip 2'), (3, 'vip 3'), (4, 'vip 4'), (5, 'vip 5'), (6, 'vip 6')], default=0, verbose_name='用户等级'),
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='users',
        ),
    ]
