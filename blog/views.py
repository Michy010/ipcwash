from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Post, Leader
from .forms import PostForm, LeaderForm
from django.contrib.auth.models import User

# Create your views here.
def index (request):
    posts = Post.objects.all().order_by('-timestamp')
    return render (request, 'blog/home.html', {'posts':posts})

def about (request):
    return render (request, 'blog/about.html')

def leaders (request):
    leaders = Leader.objects.all ()
    context = {'leaders':leaders}
    return render (request, 'blog/leaders.html', context)
@login_required
def create_leader(request):
    if request.method== 'POST':
        form = LeaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('blog:leaders')
    else:
        form = LeaderForm()

    return render (request, 'blog/create_leader.html', {'form':form })

def post (request):
    return render (request, 'blog/post.html')
@login_required
def create_post (request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect ('/')
    else:
        form = PostForm ()
    return render (request, 'blog/create_post.html', {'form':form})

def login_page (request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login (request, user)
            return redirect ('/')
        else:
            messages.error(request, 'password or username is incorrect!')

    return render (request, 'blog/login.html')

@login_required
def logout_page (request):
    logout (request)
    return redirect ('/')