# Generated by Django 2.0.6 on 2018-11-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181125_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='on_off',
            name='user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='on_off_google',
            name='on_off',
            field=models.CharField(max_length=30),
        ),
    ]