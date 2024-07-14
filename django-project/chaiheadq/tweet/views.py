from django.shortcuts import render
from models import Tweet
from forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')


def tweet_list(request):
    # all will return all the tweets from database
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    if request.method == "POST":
        # request.FILES indicates we are accepting files as well
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            # here we are just saving the form but not storing it in database as commit=False
            tweet = form.save(commit=False)
            # setting the user field
            tweet.user = request.user
            # now we are saving the tweet in the database
            tweet.save()
            # redirecting it to tweet_list
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})


def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})  
