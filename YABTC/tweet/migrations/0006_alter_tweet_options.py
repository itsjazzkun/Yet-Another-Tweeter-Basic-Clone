# Generated by Django 5.1.1 on 2024-10-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_delete_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_at']},
        ),
    ]
