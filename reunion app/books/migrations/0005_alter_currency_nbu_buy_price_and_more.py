# Generated by Django 4.2.7 on 2024-01-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='nbu_buy_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='currency',
            name='nbu_cell_price',
            field=models.CharField(max_length=255),
        ),
    ]
