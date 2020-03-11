# Generated by Django 2.2.5 on 2020-03-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller_1', '0008_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homologacion_artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=20)),
                ('new_artist_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homologacion_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('new_user_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='artist',
            name='global_rating',
            field=models.FloatField(null=True),
        ),
    ]