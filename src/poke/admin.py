from django.contrib import admin
from .models import Pokemon
from .models import Team

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Team)