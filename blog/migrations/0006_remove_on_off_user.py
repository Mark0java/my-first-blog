# Generated by Django 2.0.6 on 2018-11-24 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181124_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='on_off',
            name='user',
        ),
    ]
