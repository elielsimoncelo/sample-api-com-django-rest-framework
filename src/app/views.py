from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = { 'id': 1, 'nome': 'aluno 1' }
        return JsonResponse(aluno)
