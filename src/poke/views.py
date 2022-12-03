import requests as req
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    context = {'name' : 'TITI', 'listPoke': ['Pikachu', 'Dracafau', 'Salamèche']}
    return render(requests, 'pokeapp/home.html', context)


def pokemon(requests, number):
    r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
    result = r.json()
    
    weight = result['weight']
    image = result['sprites']['other']['home']['front_default']

    rinfo = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
    result = rinfo.json()
    for langue in result['names']:
        if langue['language']['name']=="fr":
            name = langue['name']
    color = result['color']['name']
    habitat = result['habitat']['name']

    context = {'name': name, 'color' : color, 'habitat' : habitat , 'weight' : weight , 'image' : image }        
    return render(requests,'pokeapp/pokemon.html',context)
