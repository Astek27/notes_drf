from django.shortcuts import render
from rest_framework import generics

from .serializers import CreateNoteSerializer, NoteSerializer, UpdateNoteSerializer
from .models import Note

# Create your views here.
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateNoteSerializer
        return NoteSerializer
    

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PUT', "PATCH"]:
            return UpdateNoteSerializer
        return NoteSerializer
    
    