# Generated by Django 2.2 on 2020-12-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0002_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]