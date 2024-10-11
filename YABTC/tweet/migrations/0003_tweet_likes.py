# Generated by Django 5.1.1 on 2024-10-10 10:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_tweet_retweet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
