# Generated by Django 5.1.1 on 2024-10-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('guestCanPause', models.BooleanField(default=False)),
                ('voteToSkip', models.IntegerField(default=2)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
