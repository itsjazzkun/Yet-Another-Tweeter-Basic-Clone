from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    retweet = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='retweets')
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)  # Added field for likes

    def __str__(self):
        if self.retweet:
            return f'Retweet by {self.user.username} - {self.retweet.text[:10]}'
        return f'{self.user.username} - {self.text[:10]}'

