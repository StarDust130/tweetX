from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "index.html")


def hello(request):
    return HttpResponse("Hello Babu Boi 😆")

#! Tweet List 🚵
def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets})


#! Tweet Create 🍨
@login_required
def tweet_create(request):
    if request.method == "POST":
      form = TweetForm(request.POST , request.FILES)
      if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect("tweet_list")
          
      pass
    else:
        form = TweetForm()

    return render(request, "tweet_form.html", {"form": form})
    

#! Tweet Edit ✏️
@login_required
def tweet_edit(request , tweet_id):
   tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user )

   if request.method == "POST":
      form = TweetForm(request.POST, request.FILES , instance=tweet)

      if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect("tweet_list")
      
     
   else:
      form = TweetForm(instance=tweet)

   return render(request, "tweet_form.html", {"form": form})

#! Tweet Delete 🙃
@login_required
def tweet_delete(request , tweet_id):
   tweet = get_object_or_404(Tweet , pk=tweet_id , user = request.user)

   if request.method == "POST":
      tweet.delete()
      return redirect("tweet_list")
   
   return render(request, "tweet_confrim_delete.html", {"tweet": tweet})


#! Register 🤭
def register(request):
   
   
   