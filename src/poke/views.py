import requests as req
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    context = {'name' : 'TITI', 'listPoke': ['Pikachu', 'Dracafau', 'Salamèche']}
    return render(requests, 'pokeapp/home.html', context)


def pokemon(requests, number):
    rname = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
    result = rname.json()
    name = result['name']
    image = result['sprites']['front_default']

    rcolor = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
    result = rcolor.json()

    color = result['color']['name']
    habitat = result['habitat']['name']

    context = {'name': name, 'color' : color, 'habitat' : habitat , 'image' : image}        
    return render(requests,'pokeapp/pokemon.html',context)