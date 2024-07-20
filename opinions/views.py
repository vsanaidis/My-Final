from django.shortcuts import render, get_object_or_404, redirect
from .models import Professor, ProfessorPost, Like
from django.db import IntegrityError
from .forms import  ProfessorForm,ProfessorPostForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import OpinionLike
from django.contrib.contenttypes.models import ContentType

@login_required
def professor_list(request):
    query = request.GET.get('q')
    if query:
        professors = Professor.objects.filter(name__icontains=query).order_by('-created_at')
    else:
        professors = Professor.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Professor added successfully!")
                return redirect('opinions')
            except IntegrityError:
                messages.error(request, "Professor's opinion already existing!")
    else:
        form = ProfessorForm()
    
    return render(request, 'opinions.html', {'professors': professors, 'form': form, 'query': query})
@login_required
def professor_posts(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    posts = professor.posts.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ProfessorPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.professor = professor
            post.user = request.user
            post.save()
            return redirect('professor_posts', professor_id=professor_id)
    else:
        form = ProfessorPostForm()
    
    context = {
        'professor': professor,
        'posts': posts,
        'form': form,
        'current_user': request.user,  # Pass the current user to the template
    }
    return render(request, 'professor_posts.html', context)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ProfessorPost, id=post_id)
    if request.user == post.user:
        professor_id = post.professor.id
        post.delete()
        return redirect('professor_posts', professor_id=professor_id)
    else:
        return HttpResponseForbidden("You didnot post this comment, therefore cant delete it!")
