# Generated by Django 2.2.5 on 2020-02-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_join',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.NullBooleanField(),
        ),
    ]
