from django.shortcuts import render, redirect
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, "notes/home.html", {"notes": notes})

def add_note(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Note.objects.create(title=title, content=content)

        return redirect("home")

    return render(request, "notes/add_note.html")
