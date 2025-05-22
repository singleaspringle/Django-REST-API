import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from api.models import Artist, Hit

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def artist():
    return Artist.objects.create(first_name="John", last_name="Doe")

@pytest.mark.django_db
def test_create_hit(client, artist):
    response = client.post(
        reverse('hit-list'),
        {"title": "Test Hit", "artist_id": artist.id},
        format='json'
    )
    assert response.status_code == 201
    assert Hit.objects.count() == 1
    assert Hit.objects.first().title == "Test Hit"

@pytest.mark.django_db
def test_get_hit_list(client, artist):
    Hit.objects.create(title="X", title_url="x", artist=artist)
    response = client.get(reverse('hit-list'))
    assert response.status_code == 200
    assert len(response.data) == 1

@pytest.mark.django_db
def test_get_hit_detail(client, artist):
    hit = Hit.objects.create(title="X", title_url="x", artist=artist)
    response = client.get(reverse('hit-detail', args=[hit.title_url]))
    assert response.status_code == 200
    assert response.data['title'] == "X"

@pytest.mark.django_db
def test_update_hit(client, artist):
    hit = Hit.objects.create(title="Old", title_url="old", artist=artist)
    response = client.put(
        reverse('hit-detail', args=[hit.title_url]),
        {"title": "New", "artist_id": artist.id},
        format='json'
    )
    assert response.status_code == 200
    assert response.data['title'] == "New"

@pytest.mark.django_db
def test_delete_hit(client, artist):
    hit = Hit.objects.create(title="ToDelete", title_url="to-delete", artist=artist)
    response = client.delete(reverse('hit-detail', args=[hit.title_url]))
    assert response.status_code == 204
    assert Hit.objects.count() == 0
