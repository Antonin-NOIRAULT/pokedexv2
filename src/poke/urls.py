from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('pokemon/<int:number>/',views.pokemon,name="pokemon"),
    path('search/<str:searchText>/',views.search,name="search"),
]