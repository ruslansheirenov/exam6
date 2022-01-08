from django.shortcuts import render, redirect, get_object_or_404

from .models import GuestBook
from .forms import NoteForm

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        notes = GuestBook.objects.all().filter(status='active').order_by('-created_at')
        context = {
            'notes': notes
        }
        return render(request, 'index.html', context)
    else:
        author = request.POST.get('author')
        notes = GuestBook.objects.all().filter(author=f'{author}', status='active').order_by('-created_at')
        context = {
            'notes': notes
        }
        return render(request, 'index.html', context)

def note_create_view(request):
    if request.method == 'GET':
        form = NoteForm()
        return render(request, 'create.html', {"form": form})
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_note = GuestBook.objects.create(author=author, email=email, text=text)
            return redirect("index")
        return render(request, 'create.html', {"form": form})

def note_update_view(request, pk):
    note = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = NoteForm(initial={
            'author': note.author,
            'email': note.email,
            'text': note.text
        })
        return render(request, 'update.html', {"note": note, "form": form})
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.author = request.POST.get('author')
            note.email = request.POST.get('email')
            note.text = request.POST.get('text')
            note.save()
            return redirect("index")
        return render(request, 'update.html', {"note": note, "form": form})

def note_delete_view(request, pk):
    note = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, "delete.html", {"note": note})
    else:
        note.delete()
        return redirect("index")