# Generated by Django 2.2 on 2020-12-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0005_auto_20201219_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
