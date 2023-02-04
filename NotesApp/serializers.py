from rest_framework import serializers
from NotesApp.models import Note
from django.contrib.auth.models import User
from rest_framework import permissions

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields = ['created', 'heading', 'content', 'id', 'owner',]

class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'notes']

