# Generated by Django 5.0.1 on 2024-01-11 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_rename_email_subscribemodel_form_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribemodel',
            old_name='form_subscribe',
            new_name='email',
        ),
    ]