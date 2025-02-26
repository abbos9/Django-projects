# Generated by Django 5.0 on 2023-12-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('datepicker', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('guest_num', models.IntegerField(default=1)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'reservation',
                'verbose_name_plural': 'reservations',
            },
        ),
    ]
