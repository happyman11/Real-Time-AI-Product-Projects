# Generated by Django 3.2 on 2022-07-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=10)),
                ('Content', models.CharField(max_length=200)),
                ('msgid', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
