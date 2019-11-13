from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Pizza, Masa, Ingrediente

#devuelve el listado de empresas
def index(request):
	pizza = get_list_or_404(Pizza.objects.order_by('nombre'))
	context = {'lista_pizzas': pizza }
	return render(request, 'index.html', context)

def detailPizza(request, pizza_id):
	pizza = get_object_or_404(Pizza, pk=pizza_id)
	context = {'pizza': pizza }
	return render(request, 'detailPizza.html', context)

def detailMasa(request, masa_id):
	masa = get_object_or_404(Masa, pk=masa_id)
	context = {'masa': masa }
	return render(request, 'detailMasa.html', context)

def detailIng(request, ingrediente_id):
	ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
	context = {'ingrediente': ingrediente }
	return render(request, 'detailIng.html', context)

#devuelve los empelados de un departamento
def ingredientes(request, pizza_id):
	pizza = get_object_or_404(Pizza, pk=pizza_id)
	ingredientes =  pizza.ingredientes_set.all()
	context = {'pizza': pizza, 'ingredientes' : ingredientes }
	return render(request, 'detailIng.html', context)