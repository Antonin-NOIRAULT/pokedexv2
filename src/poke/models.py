from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    color=models.CharField(max_length=20)
    catchphrase=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    id=models.IntegerField(primary_key=True)

    def getid(self):
        return self.id