# Generated by Django 5.1.3 on 2024-11-24 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_is_staff_user_is_super'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]