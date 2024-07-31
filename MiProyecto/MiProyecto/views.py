from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

import datetime

#Request: Para realizar peticiones.
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista
def bienvenida(request): #Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("Bienvenido o bienvenida a este curso de Django.")

def bienvenidaRojo(request): 
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django.</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = 'Tercera edad'
        else:
            categoria = 'Adultez'
    else:
        if edad < 10:
            categoria = 'Infancia'
        else:
            categoria = 'Adolescencia'
    resultado = "<h1>Categoría de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta = "<h1>Momento actual: {0}</h1>" .format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>" .format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S "))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    #abrimos el documento que contien a la plantilla
    plantillaExterna = open("/Users/wbriones/Documents/desarrollo/python/02-backend/Django/MiProyecto/MiProyecto/templates/miPrimeraPlantilla.html")
    #cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    #cerrar el documento que hemos abierto
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context()
    #Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametro(request):
    nombre = "NovaGym"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "Javascript", "Java", "C#", "Kotlin"]
    #abrimos el documento que contien a la plantilla    
    plantillaExterna = open("/Users/wbriones/Documents/desarrollo/python/02-backend/Django/MiProyecto/MiProyecto/templates/plantillaParametros.html")
    #cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    #cerrar el documento que hemos abierto
    plantillaExterna.close()
    #Crear un contexto
    contexto = Context({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    #Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

#Usando cargadores (loaders)
def plantillaCargador(request):
    nombre = "NovaGym"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "Javascript", "PHP", "Java", "C#", "Kotlin"]
    #especificando la carpeta donde se encuentran las plantillas y creamos una variable que la almacena
    plantillaExterna = loader.get_template('plantillaParametros.html')
    #Renderizar el documento
    documento = plantillaExterna.render({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)

def plantillaShorCut(request):
    nombre = "NovaGym"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "Javascript", "C++", "PHP", "Java", "C#", "Kotlin"]
    
    return render(request, 
                  'plantillaParametros.html',
                  {"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes}
                  )