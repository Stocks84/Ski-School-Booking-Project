# Generated by Django 4.2.10 on 2024-03-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('date_and_time', models.DateTimeField()),
                ('meeting_point', models.CharField(max_length=200)),
                ('special_requirements', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
