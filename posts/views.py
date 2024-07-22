from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Notes, Comment, Like,PostImage
from .forms import PostForm, CommentForm, PostImageForm,PostImageFormSet
#This view, I created to display the posts related to notes
def course_posts(request, course_id):
    course = get_object_or_404(Notes, id=course_id)
    #filters the posts related to a specific note
    posts = Post.objects.filter(note=course)
    
    context = {
        'course': course,
        'posts': posts,
    }
    return render(request, 'notes_posts.html', context)

# I created this view to create posts for specific notes(courses)
def add_post(request, course_id):
    course = get_object_or_404(Notes, id=course_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_formset = PostImageFormSet(request.POST, request.FILES)

        if post_form.is_valid() and image_formset.is_valid():
            post = post_form.save(commit=False)#saves the post but doenst commit it to the database
            post.note = course
            post.user = request.user
            post.save()

            image_formset.instance = post
            image_formset.save()

            return redirect('course_posts', course_id=course_id)
    else:
        post_form = PostForm()
        image_formset = PostImageFormSet(queryset=PostImage.objects.none())

    context = {
        'course': course,
        'post_form': post_form,
        'image_formset': image_formset,
    }
    return render(request, 'add_post.html', context)
#my view for the comments
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #I associate the comment with a specific course (note) and user.
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('course_posts', course_id=post.note.id)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'add_comment.html', context)
# I create the view for the likes
def like_post(request, post_id):
    #I get the specific posat for the like or if its not found i return a 404 request (page not found)
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()  # If the user has already liked the post, un-like it

    return redirect('course_posts', course_id=post.note.id)
