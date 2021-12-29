from django.db import models
from django.db.models import enums
from django.db.models.base import Model
from django.db.models.fields import BooleanField
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # specifico un related_name perchè in host c'è già una relazione con User
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        # Metto le room in ordine di update e created
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # uso CASCADE in modo tale che quando una Room viene eliminata vengono eliminita anche i messaggi associati ad essa
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        # Metto le room in ordine di update e created
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]













