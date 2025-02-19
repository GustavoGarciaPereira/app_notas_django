from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SharedNote(models.Model):
    EXPIRATION_CHOICES = [
        (3600, '1 Hora'),
        (86400, '1 Dia'),
        (604800, '1 Semana'),
    ]
    
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)
    expiration_duration = models.IntegerField(choices=EXPIRATION_CHOICES)
    
    @property
    def expiration_date(self):
        return self.shared_at + timedelta(seconds=self.expiration_duration)
    
    def is_expired(self):
        return timezone.now() > self.expiration_date
    
    def __str__(self):
        return f"{self.note.title} para {self.recipient.username}"