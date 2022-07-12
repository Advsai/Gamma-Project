# Generated by Django 3.1.2 on 2020-12-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phaseone', '0003_messageform'),
        ('bogs', '0006_messageship'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='messages',
            field=models.ManyToManyField(through='bogs.Messageship', to='phaseone.MessageForm'),
        ),
    ]
