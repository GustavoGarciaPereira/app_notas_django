from datetime import timedelta
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note, SharedNote
from .forms import NoteForm, ShareNoteForm
from django.utils import timezone

from django.db.models import Q

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        return queryset

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

def share_note(request, pk):
    note = Note.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ShareNoteForm(request.POST)
        if form.is_valid():
            shared_note = form.save(commit=False)
            shared_note.note = note
            shared_note.save()
            return redirect('note-list')
    else:
        form = ShareNoteForm()
    return render(request, 'notes/share_note.html', {'form': form})

class SharedNoteListView(LoginRequiredMixin, ListView):
    model = SharedNote
    template_name = 'notes/shared_note_list.html'

    def get_queryset(self):
        return SharedNote.objects.filter(
            recipient=self.request.user
        ).exclude(
            note__owner=self.request.user
        ).filter(
            shared_at__gte=timezone.now() - timedelta(weeks=1)
        )
        

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Em notes/views.py
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})