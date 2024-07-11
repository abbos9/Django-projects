# Generated by Django 5.0.4 on 2024-05-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
