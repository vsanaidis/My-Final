from typing import Any
from django.shortcuts import render,get_object_or_404
from .models import Notes
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponse


def notes_view(request): #my view that displays my notes

    notes = Notes.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'notes.html', context)
@login_required
def notes_details(request, title):
    note = get_object_or_404(Notes, title=title)
    
    context = {
        'note': note
    }
    return render(request, 'specific_note.html', context)
class search_views(ListView):
    model = Notes #here I am specifying that search_views will work with the Notes model in models.py
    template_name = 'notes.html' #I specify that the template I will use is notes.html, this will help to "dynamically" change the user's page
    context_object_name = 'notes' #here I just set the name of the context variable equal to notes that will be used in the template

    def get_queryset(self): #I create a custom method that will override the default one provided by ListView (imported from django.views.generic)
        query = self.request.GET.get('q', '') #I retrieve the search query parameter q from the GET request and if it is null it returns an empty string ' ' 
        level = self.request.GET.get('level', '') #same logic here but this time I retrieve the level from the GET request

        queryset = Notes.objects.all() #I set the queryset variable to all the objects inside my 'Notes' model

        if query: #I check if the query exists, in other words if the user entered something in the search bar
            queryset = queryset.filter(Q(title__icontains=query) | Q(course_field__icontains=query))  #if he did then it will return only those notes (courses) that contain the user's input in the titleor the course field 

        if level: #I check if the user entered a filter i.e. L4 or L5
            queryset = queryset.filter(level=level) #if he/she did then it will return those notes (courses) with the course level that the user chose

        return queryset #returns the filter queryset that I initialized in line 34.
