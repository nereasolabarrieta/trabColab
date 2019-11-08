from django.contrib import admin
from .models import Pizza, Masa, Ingrediente, IngredientePizza
admin.site.register(Pizza)
admin.site.register(Masa)
admin.site.register(Ingrediente)
admin.site.register(IngredientePizza)
