from django.shortcuts import render
import requests

# Create your views here.

def principal(request):
    """Función principal para consultar la API y mostrar los resultados"""
    #-----Este API call es para una obtener toda la información para elegir una película, buscando por título---      
    context = {}
    completo = {}  
    if request.method == 'POST':     
        título= request.POST['título']
        url_título = "https://streaming-availability.p.rapidapi.com/v2/search/title"
        nombre= f'{título}'
        querystring = {"title":f'{nombre}',"country":"ar","show_type":"movie","output_language":"es"}
        headers = {
            "X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
        }
        response = requests.get(url_título, headers=headers, params=querystring)
        lista= response.json()

        for i in lista['result']:
            if i['streamingInfo'] != {}:
                título = i['title']    # Se obtienen los títulos de las películas relacionados a la búsqueda
                plataforma = i['streamingInfo']['ar'].keys()   # Se obtienen las plataformas disponibles en Argentina para esa película 
                valores = [p.title() for p in plataforma]    # Se convierten los nombres de las plataformas a mayúsculas
                rating=i['imdbRating']          #  Se obtienen los puntajes del sitio IMDB.
                poster=i['posterURLs']['185']   #  Se obtiene un poster de tamaño adecuado.
                if título not in completo:
                    completo[título] = []   # Si el título no existe en el diccionario 'completo', se agrega como una clave con una lista vacía
                    
                completo[título].append({'plataformas': valores, 'rating': rating, 'poster': poster})
    context['completo'] = completo      # Se agrega el diccionario 'completo' al contexto, para renderizar en el template.

    return render(request, "App_Películas/principal.html",context)
