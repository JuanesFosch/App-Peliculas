import requests
import json
import urllib.request


"""
# -----Este API call es para obtener las plataformas que se pueden consultar y los países donde están---
url = "https://streaming-availability.p.rapidapi.com/v2/services"

headers = {             # Los headers se pasan a la función get y contienen las credenciales para interactuar con la API
	"X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())



# -----Este API call es para obtener los géneros y la cantidad de películas de cada uno---
url_géneros = "https://streaming-availability.p.rapidapi.com/v2/genres"

headers = {
	"X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url_géneros	, headers=headers)


list_of_data= response.json()

data = {
            "1": str(list_of_data['result']['1']),
            "2": str(list_of_data['result']['5'])

        }
print(data)


#-----Este API call es para una obtener toda la información para elegir una película, pero se necesita el código imdb o tmbd---

url_info_general = "https://streaming-availability.p.rapidapi.com/v2/get/basic"
headers = {
	"X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}
querystring = {"country":"ar","imdb_id":"tt1877830","output_language":"es"}

response = requests.get(url_info_general, headers=headers, params=querystring)

print(response.json())


#-----Este API call es para una obtener toda la información para elegir una película, buscando por título---
url_título = "https://streaming-availability.p.rapidapi.com/v2/search/title"

querystring = {"title":"batman","country":"ar","show_type":"movie","output_language":"es"}

headers = {
	"X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url_título, headers=headers, params=querystring)  # Esto sólo da el resultado de la respuesta HTTP (200 por ejemplo)


lista= response.json()
print(lista)
context= {}
nombres=[]
plataformas=[]
for i in lista['result']:     # CON ESTO SE OBTIENE LA PLATAFORMA DONDE ESTÁ
    if i['streamingInfo'] != {}:
        títulos= i['title']
        #print(títulos)
        nombres.append(títulos)
        plataforma= i['streamingInfo']['ar'].keys()
        #print(plataforma)
        valores= list(plataforma)
        print(valores)
        plataformas.append(valores)
        rating=i['imdbRating']
        print(rating)
        poster=i['posterURLs']['185']
        print(poster)
        #for título in valores:
            #print(título.title())
context['nombres']= nombres
context['plataformas'] = plataformas
print(context)
#for a,b in context.values():
    #print(a,b)

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
#--------------------------------------------------------------------------------------------
"""
context = {}
completo = {}  

url_título = "https://streaming-availability.p.rapidapi.com/v2/search/title"
nombre= 'batman'
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
        rating=i['imdbRating']
        #print(rating)
        poster=i['posterURLs']['185']
        #print(poster)        
        if título not in completo:
            completo[título] = []   # Si el título no existe en el diccionario 'completo', se agrega como una clave con una lista vacía
                    
        completo[título].append({'plataformas': valores, 'rating': rating, 'poster': poster})
        
    context['completo'] = completo 
print(context)
print(context['completo'][título][0]['poster'] )
