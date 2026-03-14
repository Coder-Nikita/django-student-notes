from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.db.models import Q


@login_required
def home(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, "notes/home.html", {"notes": notes})


@login_required
def notes_list(request):
    notes= Note.objects.filter(user=request.user)
    return render(request, "notes/notes_list.html", {"notes" : notes})


@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Note.objects.create(user=request.user, title=title, content=content)

        return redirect("home")

    return render(request, "notes/add_note.html")

@login_required
def update_note(request, id):

    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance = note)
        if form.is_valid():
            form.save()
            return redirect("notes_list")
        else:
            form = NoteForm(instance= note)
    return render(request, "notes/update_note.html", {"form": form})

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id,user=request.user)
    note.delete()
    return redirect("notes_list")


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = UserCreationForm()

    return render(request, "notes/register.html", {"form": form})

def notes_list(request):
    q = request.GET.get("q")

    notes = Note.objects.filter(user=request.user)

    if q:
        notes = notes.filter(
            Q(title__icontains=q) | 
            Q(content__icontains=q)
        )    
    return render(request, 'notes/notes_list.html', {"notes" : notes})