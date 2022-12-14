from django.db import models


class Colour(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    name = models.CharField(max_length = 20)
    color = models.ForeignKey(Colour, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name 

class Carr(models.Model):
    name = models.CharField(max_length = 20)
    color = models.ForeignKey(Colour, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name 

