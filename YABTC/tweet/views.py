from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Home view - could be tweet list or dashboard
def index(request):
    return redirect('tweet_list')  # Redirect to the tweet list as the homepage

# Tweet list view
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Fetch all tweets ordered by latest
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
# Tweet create view
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, 'Tweet created successfully!')
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form, 'instance': None})

@login_required
# Tweet edit view
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, 'Tweet updated successfully!')
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet_form.html', {'form': form, 'instance': tweet})

@login_required
# Tweet delete view
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted successfully!')
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# Tweet retweet view
@login_required
def tweet_retweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == "POST":
        retweet = Tweet(user=request.user, text=original_tweet.text, photo=original_tweet.photo, retweet=original_tweet)
        retweet.save()
        messages.success(request, 'Retweet successful!')
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_retweet.html', {'tweet': original_tweet})

@login_required
def tweet_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    if request.method == "POST":
        if request.user in tweet.likes.all():
            tweet.likes.remove(request.user)  # Unlike the tweet
            messages.success(request, 'You unliked the tweet!')
        else:
            tweet.likes.add(request.user)  # Like the tweet
            messages.success(request, 'You liked the tweet!')
        
        return redirect('tweet_list')

    # Render confirmation page if it's a GET request
    return render(request, 'tweet_confirm_like.html', {'tweet': tweet})

def tweet_search(request):
    query = request.GET.get('query')  # Get the search query from the GET request
    if query:
        tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_at')  # Filter tweets containing the query
    else:
        tweets = Tweet.objects.all().order_by('-created_at')  # If no query, show all tweets

    return render(request, 'tweet_list.html', {'tweets': tweets, 'query': query})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Form with POST data
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in after successful registration
            messages.success(request, 'Registration successful!')  # Success message
            return redirect('tweet_list')  # Redirect to tweet list after registration
    else:
        form = UserRegistrationForm()  # Empty form for GET requests

    return render(request, 'registration/register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('tweet_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

# User logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('user_login')
