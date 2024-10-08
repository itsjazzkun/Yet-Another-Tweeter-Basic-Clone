#MODELS
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
    def __str__(self):
        if self.retweet:
            return f'Retweet by {self.user.username} - {self.retweet.text[:10]}'
        return f'{self.user.username} - {self.text[:10]}'

    @property
    def is_retweet(self):
        return self.retweet is not None
    