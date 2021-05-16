from django.db.models import fields
from rest_framework import serializers
from app.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [ 'id', 'nome', 'rg', 'cpf', 'data_nascimento' ]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
