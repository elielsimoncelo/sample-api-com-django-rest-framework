from rest_framework import viewsets
from app.models import Aluno, Curso
from app.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# from django.http import JsonResponse

# def alunos(request):
#     if request.method == 'GET':
#         aluno = { 'id': 1, 'nome': 'aluno 1' }
#         return JsonResponse(aluno)
