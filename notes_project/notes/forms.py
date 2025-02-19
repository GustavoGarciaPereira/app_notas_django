from django import forms
from .models import Note, SharedNote

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class ShareNoteForm(forms.ModelForm):
    class Meta:
        model = SharedNote
        fields = ['recipient', 'expiration_duration']
        
        

# Em notes/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=False, help_text='Obrigatório. Informe um e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')