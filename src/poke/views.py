import requests as req
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(requests):
    liste_images = []
    rserch= req.get("https://pokeapi.co/api/v2/pokemon/")
    
    status=rserch.status_code
    if(status!=200):
        context = {'name': status}
        return render(requests,'pokeapp/searcherror.html')
    else:
        result = rserch.json()
        r = random.randint(1, 141)    
        for i in range(r, r + 10):
            r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
            result = r.json()
            liste_images.append(result['sprites']['other']['home']['front_default'])

    context = {'random' : random.randint(1, 151), 'liste_images' : liste_images[1:-1], 'first' : liste_images[0]}
    return render(requests, 'pokeapp/home.html', context)

def team(requests):
    return render(requests, 'pokeapp/team.html')

def about(requests):
    return render(requests, 'pokeapp/about.html')

def search(requests, searchText):
    number = 0
    rserch= req.get("https://pokeapi.co/api/v2/pokemon/"+searchText)
    
    status=rserch.status_code
    if(status!=200):
        context = {'name': status}
        return render(requests,'pokeapp/searcherror.html')
    else:
        result = rserch.json()
        number=result['id']            
        r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
        result = r.json()
        
        type = result['types'][0]['type']['name']
        weight = result['weight']
        image = result['sprites']['other']['home']['front_default']
        name = result['name']

        rinfo = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
        result = rinfo.json()
            
        color = result['color']['name']
        habitat = result['habitat']['name']
        nextPokemonId =number+1
        beforePokemonId =number-1

        context = {'nextPokemonId': nextPokemonId , 'beforePokemonId': beforePokemonId ,'name': name, 'color' : color, 'habitat' : habitat , 'weight' : weight , 'type' : type , 'image' : image }  
        return render(requests,'pokeapp/search.html',context)


def pokemon(requests, number):
    r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
    result = r.json()
    
    nextPokemonId=result['id'] + 1
    beforePokemonId=result['id'] - 1
    type = result['types'][0]['type']['name']
    weight = result['weight']
    image = result['sprites']['other']['home']['front_default']
    name = result['name']   

    rinfo = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
    result = rinfo.json()
    color = result['color']['name']
    habitat = result['habitat']['name']

    context = {'nextPokemonId': nextPokemonId , 'beforePokemonId': beforePokemonId , 'name': name, 'color' : color, 'habitat' : habitat , 'weight' : weight , 'type' : type , 'image' : image }        
    return render(requests,'pokeapp/pokemon.html',context)
