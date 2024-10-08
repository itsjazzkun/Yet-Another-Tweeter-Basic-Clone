from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Home view - could be tweet list or dashboard
def index(request):
    return redirect('tweet_list')  # Redirect to the tweet list as the homepage

# Tweet list view
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Fetch all tweets ordered by latest
    return render(request, 'tweet_list.html', {'tweets': tweets})

# Tweet create view
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form, 'instance': None})

# Tweet edit view
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet_form.html', {'form': form, 'instance': tweet})

# Tweet delete view
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    print(f"Request method: {request.method}")  # Debug statement
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# Tweet retweet view
# Retweet functionality
def tweet_retweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == "POST":
        retweet = Tweet(user=request.user, text=original_tweet.text, photo=original_tweet.photo, retweet=original_tweet)
        retweet.save()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_retweet.html', {'tweet': original_tweet})