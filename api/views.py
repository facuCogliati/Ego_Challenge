from django.http import JsonResponse
from .models import Vehicles


# Create your views here.

# DEVUELVE TODOS LOS VEHICULOS
def all_vehicules(request):
    try:
        vehicles = Vehicles.objects.all()
    except:
        return JsonResponse({'error': 'something went wrong'}, status = 400)
    
    data = [{'name': vehicle.name, 'price': vehicle.price, 'year_of_production': vehicle.year_of_production, 'imagen' : vehicle.imagen.url if vehicle.imagen else ''} for vehicle in vehicles]
    return JsonResponse(data, safe=False)

# DEVUELVE TODOS LOS VEHICULOS SEGUN SU CATEGORIA 
# ["Autos" - "Pickups y comerciales" - "Suvs y crossover"]
def vehicules_by_category(request, category):
    vehicles = Vehicles.objects.filter(category__name = category)
    if vehicles:
        data = [{'name': vehicle.name, 'price': vehicle.price, 'year_of_production': vehicle.year_of_production, 'imagen' : vehicle.imagen.url if vehicle.imagen else ''} for vehicle in vehicles]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Category does not exist'}, status = 400)

    
    

# DEVUELVE TODOS LOS VEHICULOS ORDENADOS SEGUN PRECIO O AÑO DE PRODUCCION
# TAMBIEN PUEDE FILTART SEGUN LA CATEGORIA
def Order_vihicules(request, field, order, category = None):
    check_fields = ['price', 'year_of_production']
    if field not in check_fields:
        return JsonResponse({'error' : 'Invalid field parameter'}, status = 400)
    
    if order == 'higher':
        field_to_order = '-' + field
    elif order == 'lower':
        field_to_order = field
    else:
        return JsonResponse({'error': 'Invalid order parameter'}, status=400)
    
    vehicles =  Vehicles.objects.filter().order_by(field_to_order)

    if category:
        vehicles = vehicles.filter(category__name = category)
        if not vehicles:
            return JsonResponse({'error': 'Invalid category parameter'}, status = 400)
    
    # Esta utima parte no me quedo muy entendible por eso aclaro: 
    # Creo un nuevo objeto y lo pongo en una lista
    # Me fijo si el modelo tiene una imagen en la base de datos y copio su URl
    data = [{'name': vehicle.name, 'price': vehicle.price, 'year_of_production': vehicle.year_of_production, 'imagen' : vehicle.imagen.url if vehicle.imagen else ''} for vehicle in vehicles]
    
    return JsonResponse(data, safe=False)