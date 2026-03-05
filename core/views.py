from django.shortcuts import render
from .models import Document
from .services.get_repos import obtener_repos_originales


""" el codigo original es ineficiente cuando se trata de consultas a muchos datos, hace 1 consulta para obtener los 10,000 
documentos y luego, por cada documento, hace 1 consulta extra para buscar el nombre del proyecto, esto suele verse 
mucho en ORMs similares a django en total, el servidor
hace 10,001 peticiones a la base de datos, lo que causa lentitud extrema lo que yo haria seria  
usar select_related() o prefetch_related() para 
realizar un join  y traer toda la información en una sola consulta

def listar_documentos():
    
    documentos = Document.objects.select_related('project').all()
    
    resultados = []
    for doc in documentos:
       
        mensaje = f"Doc: {doc.tag} (Rev {doc.revision}) - Proyecto: {doc.project.name}"
        resultados.append(mensaje)
        print(mensaje)
        
    return resultados



def otra_forma():
     esto lo haria separado para unirlo luego o eso tengo entendido, al menos para esto es un poco menos eficiente ya que hace 2 consultas 
     pero es mas facil de entender, aunque no es tan recomendable para casos con muchos datos
    documentos = Document.objects.prefetch_related('project').all()
    resultados = []
    for doc in documentos:
        mensaje = f"Doc: {doc.tag} (Rev {doc.revision}) - Proyecto: {doc.project.name}"
        resultados.append(mensaje)
        print(mensaje)
        
    return resultados


    """


#lo implementare en un mini dashboard para que lo vea mas realista, si quiere puede crear un super user o crear mock data de prueba 
#para que lo intente se que no me pidio tanto pero me gustaria esforzarme porque me siento capaz de hacerlo 
#PD: use el template que hice con tailwindcss y shadcn ui para que se vea mas bonito, hice pruebas en testing tambien si desea verlo.


def dashboard_view(request):
    documentos = Document.objects.select_related('project').all()
    repos_github = obtener_repos_originales('misterdiaz')

    context = {
        'documentos': documentos,
        'repos': repos_github,
        'titulo': "Dashboard"
    }

    return render(request, 'index.html', context)