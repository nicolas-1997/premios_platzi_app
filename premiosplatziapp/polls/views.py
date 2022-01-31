from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Estás en la pagina principals")

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero: {question_id}")
    
def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero: {question_id}")
    
def votes(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero:  {question_id}")
    