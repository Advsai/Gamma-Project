# Generated by Django 3.1.2 on 2020-12-05 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bogs', '0009_auto_20201205_1630'),
        ('phaseone', '0004_auto_20201203_1049'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageForm',
        ),
    ]
