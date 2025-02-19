from django.urls import path
from .views import (
    NoteListView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    share_note,
    SharedNoteListView
)

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('new/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('<int:pk>/share/', share_note, name='note-share'),
    path('shared/', SharedNoteListView.as_view(), name='shared-note-list'),
]