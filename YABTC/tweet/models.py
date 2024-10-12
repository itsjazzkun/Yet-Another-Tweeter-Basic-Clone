from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    retweet = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='retweets')
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)

    class Meta:
        ordering = ['-created_at']  # Default ordering by creation time

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]} (Likes: {self.likes.count()})'

    def toggle_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)

    def like_count(self):
        return self.likes.count()
