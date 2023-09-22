from django.shortcuts import render, redirect
from . models import Post
from .forms import PostForm

# Create your views here.
def home (request):
    post = Post.objects.all().order_by('-timestamp')
    return render (request, 'blog/home.html', {'post':post})

def about (request):
    return render (request, 'blog/about.html')

def leaders (request):
    return render (request, 'blog/leaders.html')

def post (request):
    return render (request, 'blog/post.html')

def create_post (request):
    if not request.user.is_superuser:
        return redirect ('/')
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