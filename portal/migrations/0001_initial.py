# Generated by Django 3.2.9 on 2021-11-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('plane', models.CharField(max_length=200)),
                ('destination_from', models.CharField(default='Лос Сантос', max_length=200)),
                ('destination_to', models.CharField(default='Сан Фіерро', max_length=200)),
                ('flight_created', models.DateTimeField(auto_now_add=True)),
                ('departure_date', models.CharField(max_length=200)),
                ('arrival_date', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
    ]
