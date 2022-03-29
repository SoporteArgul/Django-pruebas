from django.http import HttpResponse
from django.shortcuts import render
from clase.models import curso
from clase.forms import CursoFormulario
import random
# Create your views here.


def nuevo_curso(request):
    camada=random.randrange(1000,9999)
    nuevo_curso= curso(nombre='Curso JS', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"se creo el curso{nuevo_curso.nombre} camada {nuevo_curso.camada}")

def formulario_curso(request):
    #sin formulario django
    #if request.method =='POST':
     #   nuevo_curso= curso(nombre=request.POST['curso'], camada=request.POST['camada'])
      #  nuevo_curso.save()
       # print(request.POST)
        #return render(request,'indice/index.html',{'nuevo_curso': nuevo_curso})
    #return render(request,'indice/formulario_curso.html',{})
    if request.method =='POST':
        formulario=CursoFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nuevo_curso= curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
        return render(request,'indice/index.html',{'nuevo_curso': nuevo_curso})
            

    formulario=CursoFormulario()
    return render(request,'clase/formulario_curso.html',{'formulario':formulario})