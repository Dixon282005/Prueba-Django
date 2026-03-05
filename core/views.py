from django.shortcuts import render
from .models import Document
from .services.get_repos import obtener_repos_originales

def dashboard_view(request):
    documentos = Document.objects.select_related('project').all()
    repos_github = obtener_repos_originales('misterdiaz')

    context = {
        'documentos': documentos,
        'repos': repos_github,
        'titulo': "Dashboard"
    }

    return render(request, 'index.html', context)