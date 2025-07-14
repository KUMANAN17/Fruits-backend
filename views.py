from django.http import JsonResponse
from .models import Fruit  

def fruit_list(request):
    
    fruits = list(Fruit.objects.values())
    return JsonResponse(fruits, safe=False)