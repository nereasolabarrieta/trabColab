from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Pizza, Masa, Ingrediente

#devuelve el listado de empresas
def index(request):
	pizza = get_list_or_404(Pizza.objects.order_by('nombre'))
	context = {'lista_pizzas': pizzas }
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def detail(request, pizza_id):
	masa = get_object_or_404(Masa, pk=pizza_id)
	context = {'masa': masa }
	return render(request, 'detail.html', context)

#devuelve los empelados de un departamento
def empleados(request, pizza_id):
	pizza = get_object_or_404(Pizza, pk=pizza_id)
	ingredientes =  pizza.ingredientes_set.all()
	context = {'pizza': pizza, 'ingredientes' : ingredientes }
	return render(request, 'ingredientes.html', context)