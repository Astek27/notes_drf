from rest_framework import serializers
from django.utils.html import escape

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Заголовок не может быть пустым')
        return escape(value.strip())

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError('Содержание не может быть пустым')
        return escape(value.strip())
    

class CreateNoteSerializer(NoteSerializer):
    pass


class UpdateNoteSerializer(NoteSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)