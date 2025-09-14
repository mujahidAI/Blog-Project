# Remove unused imports
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm , UserCreationForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
    # NOTE: The following section is related to security and authentication.
# The @login_required decorator is used to restrict access to a view so that only authenticated users can access it.
# If a user who is not logged in tries to access a view decorated with @login_required, they will be redirected to the login page.
# This is commonly used to protect views that allow creating, editing, or deleting content, ensuring only authorized users can perform these actions.
# Usage:
#   @login_required
#   def my_view(request):
#       ...
#  Create your views here.

# ===========================
# ==== CRUD OPTIONS VIEWS ====
# ===========================

def home(request):
    return render(request, 'home.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "tweet_list.html", {'tweets': tweets})
@login_required(login_url='login')
def tweet_create(request):
    if request.method == "POST":  # Fixed: was "metthod"
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)  # false means the form is yet to be saved into the database
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {'form': form})


@login_required(login_url='login')
# for editing always use instance 
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)  
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_form.html", {'form': form})
    
@login_required(login_url='login')
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_confirm_delete.html", {'tweet': tweet}) 


def register(request):
    if request.method=="POST":
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            # form.cleaned_data is a dictionary containing validated form input.
            # Here, we access the cleaned value of the 'password1' field (the user's chosen password).
            # set_password hashes the raw password and stores it securely on the user object.
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # this login is in-built and it automatically login's 
            # the user after the user register
            login(request,user)
            return redirect('tweet_list')
    else:
        form =UserRegistrationForm()
    return render(request, "registration/register.html", {'form': form}) 
 

