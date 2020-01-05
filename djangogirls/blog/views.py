from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post        # views.py should connect models and templates.
from .forms import PostForm


def post_list(request):
    # get posts from db:
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})   # request here refers to all we receive from users via internet.
    # in function above {} is a place where you can add things for the templates to use.
    # after you set all this, you adjust your template so it can present the data that views provide!

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    '''
    To create a new post you need to call PostForm() - initialize it and pass it to template.
    :param request:
    :return:
    '''
    # first you want an empty form
    # if method is POST - that means a user filled the form, if it is valid you save it.
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)      #commit = False ensures that form is not saved before author is added.
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # following line will ensure that user go to post_detail after publishing. for this use redirect.
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
