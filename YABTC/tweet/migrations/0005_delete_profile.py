# Generated by Django 5.1.1 on 2024-10-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
