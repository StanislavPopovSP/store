# Generated by Django 3.2.13 on 2023-09-19 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='addres',
            new_name='address',
        ),
    ]
