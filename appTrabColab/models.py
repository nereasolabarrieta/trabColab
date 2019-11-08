from django.db import models

class Masa(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(max_length=40)
class Pizza(models.Model):
	# No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
	nombre = models.CharField(max_length=50)
	masa = models.ForeignKey(Masa, on_delete = models.CASCADE)
	precio = models.IntegerField(default =0)

class Ingrediente(models.Model):
	# Campo para la relación one-to-many
	nombre = models.CharField(max_length=40)

class IngredientePizza(models.Model):
	# Campo para la relación one-to-many
	ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
	pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
	cantidad = models.IntegerField()