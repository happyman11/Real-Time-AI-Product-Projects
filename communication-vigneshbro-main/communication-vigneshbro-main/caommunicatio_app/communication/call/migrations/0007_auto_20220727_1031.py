# Generated by Django 3.2 on 2022-07-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0006_chatresponse_chatbot_json'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatresponse',
            options={},
        ),
        migrations.RemoveField(
            model_name='chatresponse',
            name='chatbot_json',
        ),
        migrations.AlterField(
            model_name='history',
            name='chat_history',
            field=models.ManyToManyField(blank=True, null=True, to='call.chatresponse'),
        ),
    ]
