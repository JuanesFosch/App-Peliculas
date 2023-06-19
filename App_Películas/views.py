from django.shortcuts import render
import urllib.request
import json
import requests
# Create your views here.

completa=['The Batman', ['apple', 'hbo'], 'Batman', ['hbo'], 'El caballero oscuro: La leyenda renace', ['apple', 'hbo'],
         'Batman vuelve', ['hbo'], 'Batman y Robin', ['hbo'], 'Batman Forever', ['apple', 'hbo'], 'Batman Begins', ['apple', 'hbo'], 
         'Batman: La broma asesina', ['apple', 'hbo'], 'El hijo de Batman', ['apple', 'hbo'], 'El caballero oscuro', ['hbo'], 
         'Batman: Capucha Roja', ['hbo'], 'Batman Ninja', ['apple', 'hbo'], 'Batman: Hush', ['apple', 'hbo'], 'Batman: Año Uno', ['hbo'], 
         'Batman: La máscara del fantasma', ['hbo']]

#-----Diccionario de prueba igual que el JSON, para poder avanzar con el render----
query= {'result': [{'type': 'movie', 'title': 'The Batman','streamingInfo': {'ar': {'apple': [{'type': 'rent', 'quality': 'uhd',}],
        'hbo':[{'type': 'buy', 'quality': 'hd',}]}}
        },
        {'type': 'movie', 'title': 'Batman','streamingInfo': {'ar': {'hbo': [{'type': 'rent', 'quality': 'uhd',}],
        }}
        ,},
        {'type': 'movie', 'title': 'El caballero oscuro: La leyenda renace','streamingInfo': {'ar': {'apple': [{'type': 'buy', 'quality': 'hd',}],
        'hbo':[{'type': 'rent', 'quality': '4K',}]}}}
        ]}

def principal(request):
    context={}
    if request.method == 'POST':   # El método POST se activa cuando se aprieta el botón 'Buscar' de la form.
        título=request.POST['título']   # 'título' es el nombre del valor que se ingresa en la form, el nombre del input.
        if título == 'batman':            # Con esto se puede tomar ese valor para usarlo en la API Call.
            context['lista']=completa
    
    else:
        context['lista']=''
    
    return render(request, "App_Películas/principal.html",context)

"""
def principal(request):
    #Función principal para consultar la API y mostrar los resultados
    #-----Este API call es para una obtener toda la información para elegir una película, buscando por título---
    if request.method == 'POST':     
        título= request.POST['título']
        url_título = "https://streaming-availability.p.rapidapi.com/v2/search/title"
        querystring = {"title":"batman","country":"ar","show_type":"movie","output_language":"es"}
        headers = {
            "X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
        }
        response = requests.get(url_título, headers=headers, params=querystring)
        lista= response.json()

        for i in lista['result']:     # CON ESTO SE OBTIENE LA PLATAFORMA DONDE ESTÁ
            if i['streamingInfo'] != {}:
                título= i['title']
                print(título)
                plataforma= i['streamingInfo']['ar'].keys()
                #print(plataforma)
                valores= list(plataforma)
                for título in valores:
                    print(título.title())
        else:
            lista= {}
        return render(request, "App_Películas/principal.html",)
        """