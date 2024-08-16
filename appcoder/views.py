from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return HttpResponse("Vista de cursos")

def estudiantes(request):
    return HttpResponse("Vista de estudiantes")

def profesores(request):
    return HttpResponse("Vista de profesores")

def entregables(request):
    return HttpResponse("Vista de entregables")