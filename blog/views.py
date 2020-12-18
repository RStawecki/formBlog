from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/home.html', {'posts': posts, 'form': PostForm()})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def create_form(request):
    
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/create_form.html', {'form': form})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')