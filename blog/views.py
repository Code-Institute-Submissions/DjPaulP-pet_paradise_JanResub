from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post

def blog(request):
    """ A view to return the Blog Posts page """
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})

def post_detail(request, slug):
    """ A view to return the actual Blog Post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)

    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
