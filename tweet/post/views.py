from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by()
    return render(request, 'index.html',{'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            print(post)
            post.save()
            return index(request)
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_del_post(request,post_id):
    post = get_object_or_404(Post, pk=post_id,user = request.user)

    
    if request.method == 'GET' and 'delete' in request.GET:
        post.delete()
        return index(request)


    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            print(post)
            post.save()
            return index(request)
    else:
        form = PostForm(instance=post)
    return render(request, 'add_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html', {'form': form})
