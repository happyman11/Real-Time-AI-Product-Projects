# Generated by Django 3.2 on 2022-07-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_auto_20220727_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='called_caller',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='called_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
