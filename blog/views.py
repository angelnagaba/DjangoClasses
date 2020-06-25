from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

    #Creating a new post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#the view for editing posts
#this view requires authentication i.e cannot be viewed by everyone except those allowed to do so
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#the view for drafts of posts 
#this view requires authentication i.e cannot be viewed by everyone except those allowed to do so
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

#publishing drafts
#this view requires authentication i.e cannot be viewed by everyone except those allowed to do so
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
#this view requires authentication i.e cannot be viewed by everyone except those allowed to do so
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#def LoginView():


#class-based views
#class TestView(View):
#   def get(self, request, *args, **kwargs):
 #       return
  #      HttpResponse("Hello, these are class based views")