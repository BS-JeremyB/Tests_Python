import pytest
from ..models import Client
from django.urls import reverse


@pytest.mark.django_db
def test_liste_clients(client):
    Client.objects.create(nom="John", email="johndoe@example.com")
    Client.objects.create(nom="Jane", email="janedoe@example.com")

    reponse = client.get(reverse("liste_clients"))

    assert reponse.status_code == 200
    assert reponse.json() == [
        {"nom": "John", "email": "johndoe@example.com"},
        {"nom": "Jane", "email": "janedoe@example.com"},
    ]