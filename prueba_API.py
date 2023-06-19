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

"""
#-----Este API call es para una obtener toda la información para elegir una película, buscando por título---
url_título = "https://streaming-availability.p.rapidapi.com/v2/search/title"

querystring = {"title":"batman","country":"ar","show_type":"movie","output_language":"es"}

headers = {
	"X-RapidAPI-Key": "73b6f11569msh8f43883d047ca0ap1e4914jsn51eda2f91df9",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url_título, headers=headers, params=querystring)


lista= response.json()
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
        #for título in valores:
            #print(título.title())
context['nombres']= nombres
context['plataformas'] = plataformas
#print(context)
for a,b in context.values():
    print(a,b)
