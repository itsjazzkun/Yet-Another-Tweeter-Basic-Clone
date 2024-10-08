#VIEWS

from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404 , redirect
def index(request):
    return render(request, 'index.html')


def tweet_list(request):
   tweets = Tweet.objects.all().order_by('-created_at')
   return render (request, 'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    if request.method == "POST":
        TweetForm(request.POST , request.FILES)
        if form.is_valid():
            tweet =  form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = TweetForm()
    return render (request, 'tweet_form.html',{'form':form })

def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES, instance=tweet)
        if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save ()
          return redirect('tweet_list')
          
    else: 
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html' ,{'form': form})

def tweet_delete(request, tweet_id):
    tweet= get_object_or_404 (Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confrim_delete.html', {'tweet': tweet})

def tweet_retweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        retweet = Tweet(user=request.user, retweet=original_tweet)
        retweet.save()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_retweet.html', {'tweet': original_tweet})