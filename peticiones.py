#"codigo del consumo de la api "
from datetime import datetime
import requests
import json
from urllib.request import urlopen
import base64



urlEpisodio=[]
urlimagen=[]

# Realizar una peticion Get a la api de rickandMorty con las siguientes id
# y obtiene resupesta del la api un archivo JSON
url = "https://rickandmortyapi.com/api/character/1,2,13,26,32,33/"
response = requests.get(url)
print(response.text)
listaPersonaje = json.loads(response.text)

#Esta lista almacena el los datos de personaje nombre y especie
DatosPersonaje=[]
#recorro la lista de respuesta listaPersonaje para obtener nombre, especie,la primer url de episodio 
# donde aparece el personaje

for personaje in listaPersonaje:

    #print(
    #Nombre:{}
    #Especie:{}
    #Imagen:{}
    #Episodio:{}
    #Fecha_emision:{}
    #Planeta:{}
    #.format(personaje['name'], personaje['species'], personaje['image'][0], personaje['episode'], personaje['location']['name']))

    #print("nombre:", personaje['name'])
    #print('')
    urlimagen.append(personaje['image'])
    urlEpisodio.append(personaje['episode'][0])
    datos = {'nombre': personaje['name'], 'especie': personaje['species']}
    print(datos)
    DatosPersonaje.append(datos)


#Almaceno los datos del episodio nombre_Episodio y Fecha en un formato 01/05/2015
DatosEpisodio=[]
#almaceno la respuesta del la api en una lista
listaEpisodio=[]
#utilizo este for para recorrer la lista de las url de los episodios
#para consultar la siguiente informacion de cada uno de los episodios almacenados en la lista
for img in urlimagen:
    file = urlopen(img['imagen']).read()
    srcdata = base64.b64decode(file)
    print(srcdata, type(srcdata))
    srcdata = str(srcdata).replace("b\'", "")
    srcdata = srcdata.replace("\'", "")
    print(srcdata)
    break


for x in urlEpisodio:
    urlEpisode=x
    response = requests.get(urlEpisode)
    listaEpisodio.append(json.loads(response.text))

#Recorro la lista donde almacene el formato JSON de respuesta de la api
for x in listaEpisodio:
    fechaObtenida=x['air_date']
    formatoLectura='%B %d, %Y'
    objDate=datetime.strptime(fechaObtenida, formatoLectura)
    nuevoFormato=objDate.strftime('%d/%m/%Y')
    formato={'NombreEpisodio':x['name'],'Fecha':nuevoFormato }
    DatosEpisodio.append(formato)

#La DatosFinal obtiene los datos necesarios para mandarlos a la api 
#https://api4pluto.dudewhereismy.com.mx/rickandmorty
#en el  orden deseado para su consulta
DatosFinal=[]
#Utilizo este for para anidar los datos de la lista DatosPersonaje y la lista de DatosEpisodio 
#y crear solo una lista en el orden espeficicado para su posterior consulta
for indice in range(0,len(DatosPersonaje)):
    
    estructura={ "Nombre":DatosPersonaje[indice]['nombre'],
    "Specie":DatosPersonaje[indice]['especie'],
    "imagen":"String",
    "episodio":DatosEpisodio[indice]['NombreEpisodio'],
    "Fecha_Emision":DatosEpisodio[indice]['Fecha']
    }
    DatosFinal.append(estructura)
        
#la url de la api rickandmorty
urlPost="https://api4pluto.dudewhereismy.com.mx/rickandmorty"

#utilizo este for para carga los datos de la lista DAtosDinal pero de uno en uno iniciando 
#desde indice =0 y los va registrando con el method POST 
for y in DatosFinal:
    filtro={
    "name": y['Nombre'],
    "species": y['Specie'],
    "image": y['imagen'],
    "episode_name": y['episodio'],
    "air_date": y['Fecha_Emision']
    }
    #respuesta=requests.post(urlPost, json=filtro)
    #texto_response=respuesta.text
    #print(texto_response)

