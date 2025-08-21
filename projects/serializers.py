from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'titulo', 'contenido', 'f_publicacion', 'autor']
        read_only_fields = ['f_publicacion'] 