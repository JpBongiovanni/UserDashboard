# Generated by Django 2.2 on 2020-12-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_auto_20201219_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
