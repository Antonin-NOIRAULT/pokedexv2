import requests as req
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    context = {'name' : 'TITI', 'listPoke': ['Pikachu', 'Dracafau', 'Salamèche']}
    return render(requests, 'pokeapp/index.html', context)

def hello(requests):
    text = '<p> Liste des pokemons en cours de chargement</p> \
    <div>Lorem ipsum... </div>'
    return HttpResponse(text)

def details(requeste, number):
    text = '<h1> voici pokemon n°%d<h1>' % number
    return HttpResponse(text)

def pokemon(requests, number):
    r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
    result = r.json()
    name = result['name']
    context = {'name': name}        
    return render(requests,'pokeapp/index.html',context)