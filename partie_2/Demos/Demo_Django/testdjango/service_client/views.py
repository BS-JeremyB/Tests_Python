from django.http import JsonResponse
from .models import Client

# Create your views here.
def liste_clients(request):
    clients = Client.objects.all()
    donnees = [{'nom': client.nom, 'email': client.email} for client in clients]
    return JsonResponse(donnees, safe=False)

